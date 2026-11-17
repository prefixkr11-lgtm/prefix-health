/* Prehealth — Service Worker (v20)
   앱 셸 + MediaPipe CDN 리소스(@mediapipe/tasks-vision 모듈·wasm·자세 모델)를 런타임 캐시한다.
   카메라·동영상 스트림과 Range 요청은 건드리지 않는다. */
const CACHE = 'prefix-health-v20';
const CDN_CACHE = 'prefix-health-v20-cdn';
const CDN_HOSTS = ['cdn.jsdelivr.net', 'storage.googleapis.com'];
/* 캐시해도 되는 MediaPipe 자산인지 (버전이 박힌 불변 파일들) */
const CDN_RE = /(\/npm\/@mediapipe\/tasks-vision@|mediapipe-models\/|pose_landmarker|vision_bundle|\.wasm(\?|$)|\.task(\?|$)|\.mjs(\?|$))/i;
const SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png?v=8',
  './icons/icon-512.png?v=8',
  './icons/icon-1024.png?v=8',
  './icons/apple-touch-icon.png?v=8'
];

self.addEventListener('install', function (e) {
  e.waitUntil(
    caches.open(CACHE)
      .then(function (c) { return c.addAll(SHELL).catch(function () {}); })
      .then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (e) {
  e.waitUntil(
    caches.keys()
      .then(function (keys) {
        return Promise.all(keys.filter(function (k) { return k !== CACHE && k !== CDN_CACHE; })
          .map(function (k) { return caches.delete(k); }));
      })
      .then(function () { return self.clients.claim(); })
  );
});

/* CDN 자산: 한 번 받으면 캐시에서 바로 (불변 주소) */
function cdnCacheFirst(req) {
  return caches.open(CDN_CACHE).then(function (c) {
    return c.match(req).then(function (hit) {
      if (hit) return hit;
      return fetch(req).then(function (res) {
        if (res && (res.ok || res.type === 'opaque')) {
          const copy = res.clone();
          c.put(req, copy).catch(function () {});
        }
        return res;
      });
    });
  });
}

self.addEventListener('fetch', function (e) {
  const req = e.request;
  if (req.method !== 'GET') return;

  let url;
  try { url = new URL(req.url); } catch (err) { return; }
  if (url.pathname.endsWith('/sw.js')) return;
  // Range 요청(동영상 시킹)은 그대로 통과
  if (req.headers.get('range')) return;

  // 외부 CDN: MediaPipe 모듈·wasm·모델만 캐시한다 (재방문 시 빠르게 시작)
  if (url.origin !== self.location.origin) {
    if (CDN_HOSTS.indexOf(url.hostname) >= 0 && CDN_RE.test(url.pathname + url.search)) {
      e.respondWith(cdnCacheFirst(req));
    }
    return;
  }

  // HTML 문서: 네트워크 우선 → 최신 코드가 바로 반영되고, 오프라인이면 캐시
  const isDoc = req.mode === 'navigate' ||
    (req.headers.get('accept') || '').indexOf('text/html') !== -1;
  if (isDoc) {
    e.respondWith(
      // 문서는 HTTP 캐시도 건너뛰고 확인한다 (배포 직후 새 코드가 바로 보이도록)
      fetch(req, { cache: 'no-cache' })
        .then(function (res) {
          const copy = res.clone();
          caches.open(CACHE).then(function (c) { c.put(req, copy); }).catch(function () {});
          return res;
        })
        .catch(function () {
          return caches.match(req).then(function (hit) {
            return hit || caches.match('./index.html').then(function (h) {
              return h || caches.match('./');
            });
          });
        })
    );
    return;
  }

  // 정적 자산: stale-while-revalidate
  e.respondWith(
    caches.match(req).then(function (hit) {
      const net = fetch(req).then(function (res) {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(CACHE).then(function (c) { c.put(req, copy); }).catch(function () {});
        }
        return res;
      }).catch(function () { return hit; });
      return hit || net;
    })
  );
});
