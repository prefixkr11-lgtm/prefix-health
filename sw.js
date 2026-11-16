/* Prehealth — Service Worker
   앱 셸만 캐싱한다. MediaPipe CDN·카메라·동영상 스트림은 건드리지 않는다. */
const CACHE = 'prefix-health-v6';
const SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png?v=6',
  './icons/icon-512.png?v=6',
  './icons/icon-1024.png?v=6',
  './icons/apple-touch-icon.png?v=6'
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
        return Promise.all(keys.filter(function (k) { return k !== CACHE; })
          .map(function (k) { return caches.delete(k); }));
      })
      .then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (e) {
  const req = e.request;
  if (req.method !== 'GET') return;

  let url;
  try { url = new URL(req.url); } catch (err) { return; }
  // 외부 CDN(MediaPipe 등)은 서비스워커가 개입하지 않는다
  if (url.origin !== self.location.origin) return;
  if (url.pathname.endsWith('/sw.js')) return;
  // Range 요청(동영상 시킹)도 그대로 통과
  if (req.headers.get('range')) return;

  // HTML 문서: 네트워크 우선 → 최신 코드가 바로 반영되고, 오프라인이면 캐시
  const isDoc = req.mode === 'navigate' ||
    (req.headers.get('accept') || '').indexOf('text/html') !== -1;
  if (isDoc) {
    e.respondWith(
      fetch(req)
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
