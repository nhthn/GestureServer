const state = {
    numTouches: 0,
    centerX: 0,
    centerY: 0,
    rangeX: 0,
    rangeY: 0,
    area: 0
};

const receiver = document.getElementById("receiver");

function handleTouch(event) {
    event.preventDefault();
    state.numTouches = event.touches.length;
    if (state.numTouches > 0) {
        const x = [];
        const y = [];
        const area = [];
        for (let touch of event.touches) {
            x.push(touch.screenX);
            y.push(touch.screenY);
            area.push(touch.radiusX * touch.radiusX + touch.radiusY * touch.radiusY);
        }
        state.centerX = 0;
        for (let xx of x) {
            state.centerX += xx / state.numTouches;
        }
        state.centerY = 0;
        for (let yy of y) {
            state.centerY += yy / state.numTouches;
        }
        state.rangeX = Math.max.apply(null, x) - Math.min.apply(null, x);
        state.rangeY = Math.max.apply(null, y) - Math.min.apply(null, y);
        state.area = 0;
        for (let area_ of area) {
            state.area += area_ / state.numTouches;
        }
    }
}

receiver.addEventListener("touchstart", handleTouch, false);
receiver.addEventListener("touchmove", handleTouch, false);
receiver.addEventListener("touchend", handleTouch, false);

const sampleRate = 60;

const socket = new WebSocket("ws://{{ ip_address }}:{{ websockets_port }}/");

socket.addEventListener("open", () => {
    setInterval(() => {
        socket.send(
            state.numTouches / 5
            + "," + state.centerX / window.screen.width
            + "," + state.centerY / window.screen.height
            + "," + state.rangeX / window.screen.width
            + "," + state.rangeY / window.screen.height
            + "," + state.area / window.screen.width
        );
    }, 1000 / sampleRate);
});

socket.addEventListener("error", () => {
    receiver.textContent = "Could not connect to WebSocket.";
});
