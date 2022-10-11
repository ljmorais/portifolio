const turnOn = document.getElementById('turnOn')
const turnOff = document.getElementById('turnOff')
const lamp = document.getElementById('lamp')

function islampQuebra(){
    return lamp.src.indexOf ('quebrada') > -1

}

function lampOn() {
    if (!islampQuebra () ){
        lamp.src = 'ligada.jpg'
    }
}

function lampOff(){
    if (!islampQuebra()){
        lamp.src='desligada.jpg'
    }
}

function lampQuebra(){
    lamp.src='quebrada.jpg'
}

turnOn.addEventListener ('click', lampOn )
turnOff.addEventListener('click', lampOff )
lamp.addEventListener('mouseover', lampOn )
lamp.addEventListener('mouseleave', lampOff )
lamp.addEventListener('dblclick', lampQuebra )
