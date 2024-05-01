const pendingRequests = new Map();
const CACHE_NAME = "sketchbook-cache-20240430";

const requestsChannel = new BroadcastChannel("requests");
const responsesChannel = new BroadcastChannel("responses");


function getRequiresNetwork(request) {
    const url = new URL(request.url);
    const nakedPathName = url.pathname.replace("/", "");
    const isIndex = nakedPathName === "index.html" || url.pathname === "/";
    const isSketch = nakedPathName === "sketch.html";
    const isServiceWorker = nakedPathName === "service_worker.js";
    const isWebWorker = nakedPathName === "file_worker.js";
    const isNested = url.pathname.substring(1, url.pathname.length).indexOf("/") != -1;
    const exceptions = [isIndex, isServiceWorker, isNested, isSketch, isWebWorker];
    const numExceptions = exceptions
        .filter((x) => x == true);
    return numExceptions.length > 0;
}


async function interceptRequest(request) {
    const url = new URL(request.url);
    const currentHost = self.location.hostname;

    let future = null;
    if (currentHost !== url.hostname) {
        future = fetch(url.pathname).then(async (networkResponse) => {
            return networkResponse;
        });
    } else if (getRequiresNetwork(request)) {
        const cache = await caches.open(CACHE_NAME);

        const makeCachedRequest = () => {
            return fetch(request).then(async (networkResponse) => {
                if (url.hostname === currentHost && networkResponse.ok && request.method === "GET") {
                    cache.put(url.pathname, networkResponse.clone());
                }
                return networkResponse;
            });
        }

        future = cache.match(url.pathname).then((cachedValue) => {
            if (cachedValue !== undefined) {
                return new Promise((resolve) => {
                    resolve(cachedValue);
                });
                makeCachedRequest();
            } else {
                return makeCachedRequest();
            }
        });
        
    } else {
        future = getItem(url.pathname.replace("/", "")).then((content) => {
            return new Response(content);
        });
    }

    return (await future);
}


self.addEventListener("fetch", (event) => {
    const request = event.request;
    event.respondWith(interceptRequest(request));
});


class ReadOnlyOpfsFileManager {

    constructor() {
        const self = this;
        self._waitingPromises = new Map();

        responsesChannel.onmessage = (event) => {
            const data = event.data;
            const resolve = self._waitingPromises.get(data["target"]);
            self._waitingPromises.delete(data["target"]);
            resolve(data["content"]);
        };
    }
    
    getItem(filename) {
        const self = this;
        const target = Date.now() + "." + filename;

        return new Promise((resolve) => {
            self._waitingPromises.set(target, resolve);
            requestsChannel.postMessage({
                "filename": filename,
                "target": target
            });
        });
    }
    
}


const manager = new ReadOnlyOpfsFileManager();


function getItem(path) {
    return manager.getItem(path);
}
