const diagramsContainer = document.getElementById("diagramsContainer");

for (let i = 0; i < categories.length; i++) {
    const category = categories[i];
    diagramsContainer.innerHTML += `<h3>${category}</h3>`;
    diagramsContainer.innerHTML += `<div class="imagesContainer"></div>`;
    const imagesContainer = diagramsContainer.lastChild;

    for (let j = 0; j < imagesNames.length; j++) {
        const image = imagesNames[j];
        if (image.startsWith(category.split(".")[0])) {
            imagesContainer.innerHTML += `
            <div class="imageCard">
                <img class="clickable" src="./images/${folder}/${image}" />
                <div class="imageInfo">${image.split(".png")[0]}</div>
            </div>
            `;
        }
    }
}

const images = document.getElementsByClassName("clickable");
for (let i = 0; i < images.length; i++) {
    const image = images[i];
    image.addEventListener("click", () => {
        image.classList.toggle("fullScreen");
    });
}
