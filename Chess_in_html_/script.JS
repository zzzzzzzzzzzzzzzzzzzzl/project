


function newdiv(id,count){
    let d=document.createElement('div');
    d.id=id+count;
    d.className="square";
    d.innerHTML='&nbsp';
    if (count%2==0){
    d.style.background='red';}
    else{
        d.style.background='black';}
    
    d.style.width='50px';
    d.style.height='50px';
    d.style.scale="90%";
    document.body.appendChild(d);
    return d
}
for (let j=0;j<800;j++){

for(let i=0;i<8;i++){
    var child=newdiv("here",i);
    var parent=document.getElementById('content');
    parent.appendChild(child);
}
}




