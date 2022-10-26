const recommend_elements = document.getElementsByClassName("recommend");
Array.from(recommend_elements).forEach(function (element) {
  element.addEventListener(type='click', listener=function () {
    if (confirm(message="정말로 추천하시겠습니까?")) {
      location.href = this.dataset.uri;
    };
  });
});