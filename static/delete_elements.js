const delete_elements = document.getElementsByClassName("delete");
Array.from(delete_elements).forEach(function (element) {
  element.addEventListener(type='click', listener=function () {
    if (confirm(message="정말로 삭제 하시겠습니까?")) {
      location.href = this.dataset.uri;
    }
  });
});