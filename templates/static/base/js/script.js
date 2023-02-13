const botao = document.querySelectorAll(".sidebar ul li");
const hidenSidebar = document.querySelector('.navbar-toggler')
// Mostrar paineis

const iconSelec = document.querySelectorAll('#side_nav > ul > li > a')
const subpain = document.querySelectorAll("#side_nav > ul > li > ul > li > a")
 const btn_subpain = document.querySelector("body > div.content.d-flex.flex-column > nav > div > div > div > span")

// Botões da margem
lista_icons = ["Radiocomunicação", "Telecomunicação", "Gestão Financeira", "Gestão de Documentos", "Gestão Logística", "Catálogo", "Licitações", "Legislação", "Configurações", "Notificações"]


const painel = document.querySelector("body > div.content.d-flex.flex-column")
const icones = document.querySelectorAll("#side_nav > ul > li > ul")
const titulo = document.querySelector('.navbar-brand')

const botaoFecha = document.querySelector('.btn.close-btn')
const conteudoFecha = document.querySelector('.container.main-content-all')

painel.addEventListener("click",function(){
    icones.forEach((enn)=>{
        try{

            enn.classList.remove("mostra")
        }catch(e){
            
        }
    })
})


iconSelec.forEach((elem12, index)=>{
    elem12.addEventListener("click", function(e){
        document.querySelector(`#side_nav > ul > li:nth-child(${index+1}) > ul `).classList.toggle("mostra")
        // console.log(e.target.innerText)
        iconSelec.forEach((el2, index)=>{
            if(el2.innerText == e.target.innerText){
                titulo.innerText = el2.innerText
                btn_subpain.innerText = ""
            }else{
                try{
                    document.querySelector(`#side_nav > ul > li:nth-child(${index+1}) > ul `).classList.remove("mostra")
                }catch(e){
                    
                }
            }
        })
    
    
    }
    )

})

botao.forEach((elem)=>{
    elem.addEventListener("click", function(e){
        if((lista_icons.includes((e.target.innerText).trim()))){
            document.querySelector("#side_nav > ul> li > a.active").classList.remove('active')
            e.target.classList.add('active')
        }
        }

    )

})

hidenSidebar.addEventListener('click',(e)=>{
    document.querySelector("#side_nav").classList.add('active')


})

botaoFecha.addEventListener('click',(e)=>{
    document.querySelector("#side_nav").classList.remove('active')
})

conteudoFecha.addEventListener('click',(e)=>{
    document.querySelector("#side_nav").classList.remove('active')
})

subpain.forEach((elem45)=>{
    elem45.addEventListener("click", function(e){
        btn_subpain.innerText = e.target.innerText
        })
        }

    )

