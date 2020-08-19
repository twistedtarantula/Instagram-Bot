function instaBot() {
  var uname = document.getElementById("uname").value;
  var pwd = document.getElementById("pwd").value;
  var tag = document.getElementById("tag").value;
  eel.instaBot(uname, pwd, tag);
  window.close();
}
