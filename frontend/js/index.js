const calcTime = (timestamp) => {
  const curTime = new Date().getTime() - 9 * 60 * 60 * 1000;
  const time = new Date(curTime - timestamp);
  const hour = time.getHours();
  const min = time.getMinutes();
  const second = time.getSeconds();
  if (hour > 0) {
    return `${hour} 시간전`;
  } else if (min > 0) {
    return `${min}분 전`;
  } else if (second >= 0) {
    return `${second}초 전`;
  } else {
    return `방금 전`;
  }
};

const renderData = (data) => {
  const main = document.querySelector("main");
  data.reverse().forEach(async (obj) => {
    const Div = document.createElement("div");
    Div.className = "item-list";

    const imageDiv = document.createElement("div");
    imageDiv.className = "item-list__img";

    const img = document.createElement("img");
    // img.src = obj.image
    const res = await fetch(`/images/${obj.id}`);
    const blob = await res.blob();
    const url = URL.createObjectURL(blob);
    img.src = url;

    const InfoDiv = document.createElement("div");
    InfoDiv.className = "item-list__info";

    const InfoTitleDiv = document.createElement("div");
    InfoTitleDiv.className = "item-list__info-title";
    InfoTitleDiv.innerText = obj.title;

    const InfoMetaDiv = document.createElement("div");
    InfoMetaDiv.className = "item-list__info-meta";
    InfoMetaDiv.innerText = `${obj.place} ${calcTime(obj.insertAt)}`;

    const InfoPriceDiv = document.createElement("div");
    InfoPriceDiv.className = "item-list__info-price";
    InfoPriceDiv.innerText = obj.price;

    InfoDiv.appendChild(InfoTitleDiv);
    InfoDiv.appendChild(InfoMetaDiv);
    InfoDiv.appendChild(InfoPriceDiv);
    imageDiv.appendChild(img);
    Div.appendChild(imageDiv);
    Div.appendChild(InfoDiv);

    main.appendChild(Div);
  });
};

const fetchList = async () => {
  const access_token = window.localStorage.getItem("token");
  const res = await fetch("/items", {
    headers: {
      Authorization: `Bearer ${access_token}`,
    },
  });
  console.log(res.status);
  if (res.status === 401) {
    window.location.pathname = "./login.html";
    return;
  }
  const data = await res.json();
  renderData(data);
};

fetchList();
