var socket = io("http://localhost:9000", {});

socket.on("connect", function () {
  console.log("connect");
});

socket.on("message", (message) => {
  message.forEach(element => {
    // const Timestamp = element.Timestamp
    // const dateTime = new Date(Timestamp)    
    // const getMinutes = dateTime.getMinutes()
    console.log(element.Timestamp)

  });
});
