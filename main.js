async function FetchData(url) {
  let response = await fetch(url);
  if (!response.ok) {
    console.error(`Error ${response.status}: ${response.statusText}`);
    return;
  }
  return await response.json();
}

async function getData() {
    const backendUrl = `http://127.0.0.1:8000/`;
    const data = await FetchData(backendUrl)

    console.log(data);
}



let button = document.getElementById("data");
button.addEventListener("click", getData);

