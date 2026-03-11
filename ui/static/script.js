async function runAll(){

let res = await fetch('/run_all')

let data = await res.json()

document.getElementById("output").innerText = data.result
}


async function runMarker(marker){

let res = await fetch('/run_marker/' + marker)

let data = await res.json()

document.getElementById("output").innerText = data.result
}


async function runTest(test){

let res = await fetch('/run_test/' + test)

let data = await res.json()

document.getElementById("output").innerText = data.result
}


async function addApi(){

let name = document.getElementById("api_name").value

await fetch('/add_api?api_name=' + name,{
method:'POST'
})

location.reload()
}


async function deleteApi(name){

await fetch('/delete_api/' + name,{
method:'DELETE'
})

location.reload()
}