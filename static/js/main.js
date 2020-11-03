// cisc_data = JSON.parse(csic)
// ecml_data = JSON.parse(ecml)

function createResult(request,original,predicted){
   const divobj = ' <div class="mx-5 my-3 card grey lighten-3 card-body py-3 px-5">'+
                        '<span>'+request+'</span>'+
                        '<div class="d-flex justify-content-between">'+
                            '<span class="text-primary">'+
                                'Original:'+convertToText(original)+
                            '</span>'+
                            '<span class="bg-primary text-white font-weight-bold">'+
                                'Predicted:'+showPrediction(predicted)+
                            '</span>'+
                        '</div>'+
                    '</div>'
    $("#list").append(divobj) 
}

function convertToText(value){
    if (Math.ceil(value)==0) {
        return "Benign"
    }else if(Math.ceil(value)==1){
        return "Malicious"
    }
}
function showPrediction(prediction){
    benign = (prediction.benign)*100.0
    malicious = prediction.malicious*100.0
    return "Benign: "+benign.toFixed(2)+", Malicious:"+malicious.toFixed(2)
    
}
function getpath(model){
    if (model=="csiccnn") {
        return '/csic/cnn/predict'
    }else if(model =="csicdnn"){
        return '/csic/dnn/predict'
    }else if(model =="ecmlcnn"){
        return '/ecml/cnn/predict'
    }else if(model=="ecmldnn"){
        return '/ecml/dnn/predict'
    }
}
async function makeRequest(request,model){
    const response = await fetch(getpath(model),{
        method: 'POST',
        headers:{
            'Content-Type':'text/plain'
        },
        body:request
    })
    if (response.ok) {
        return response.json()
    }
}

async function sample(){
    const dataset = $("input[name='dataradio']:checked").val()
    const model = $("input[name='modelradio']:checked").val()

    const random = await pick(dataset)
    for (let index = 0; index < random.length; index++) {
        predicted = await makeRequest(random[index].request,model)
        createResult(random[index].request,random[index].label,predicted)
    }
}

async function pick(dataset){
    if (dataset=="csic") {
        res = await fetch("static/js/csic.json")
        if(res.ok){
            temp = await res.json()
        }     
    } else if (dataset=="ecml") {
        res = await fetch("static/js/ecml.json")
        if(res.ok){
            temp = await res.json()
        }   
    }
    picks = []
    for (let index = 0; index < 5; index++) {
        randind = Math.floor(Math.random()*temp.length)
        picks.push(temp[randind])
        temp.splice(randind,1)  // array[index];   
    }
    return picks
}