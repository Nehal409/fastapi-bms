var socket = io("http://localhost:9000", {});

socket.on("connect", function () {
  console.log("connect");
});

socket.on("message", (message) => {
  console.log(message);
});
