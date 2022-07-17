(function(){"use strict";var e={4354:function(e,t,a){var n=a(9242),o=a(3396);function r(e,t,a,n,r,l){const i=(0,o.up)("router-view");return(0,o.wg)(),(0,o.j4)(i)}var l={name:"App"},i=a(89);const s=(0,i.Z)(l,[["render",r]]);var u=s,d={SERVER_IP:"http://localhost:8080",YMAP_SETTINGS:{apiKey:"0bc612ef-d8aa-4eba-946a-fbe66723d23c",lang:"ru_RU",coordorder:"latlong",enterprise:!1,version:"2.1"}};const c=e=>((0,o.dD)("data-v-19591566"),e=e(),(0,o.Cn)(),e),p=c((()=>(0,o._)("input",{type:"file",id:"file",name:"file"},null,-1))),f=(0,o.Uk)("Load and Submit");function m(e,t,a,n,r,l){const i=(0,o.up)("b-button"),s=(0,o.up)("b-form");return(0,o.wg)(),(0,o.j4)(s,{action:"upload_file",role:"form",method:"post",onSubmit:l.onSubmit},{default:(0,o.w5)((()=>[p,(0,o.Wm)(i,{type:"submit",variant:"primary"},{default:(0,o.w5)((()=>[f])),_:1})])),_:1},8,["onSubmit"])}var v=a(6265),h=a.n(v),b={name:"FirstTask",data(){return{}},methods:{onSubmit(e){e.preventDefault()},submitFile(){let e=new FormData;e.append("file",this.file),console.log(">> formData >> ",e),h().post("/api/task1_upload",e,{headers:{"Content-Type":"multipart/form-data"}}).then((function(){console.log("SUCCESS file upload!!")})).catch((function(){console.log("FAILURE file upload!!")}))},handleFileUpload(){this.file=this.$refs.file.files[0],console.log(">>>> 1st element in files array >>>> ",this.file)}}};const _=(0,i.Z)(b,[["render",m],["__scopeId","data-v-19591566"]]);var g=_;function w(e,t,a,n,r,l){const i=(0,o.up)("b-form");return(0,o.wg)(),(0,o.j4)(i,{onSubmit:l.onSubmit,onReset:l.onReset},null,8,["onSubmit","onReset"])}var y={name:"SecondTask",data(){return{form:{email:"",name:"",food:null,checked:[]}}},methods:{onSubmit(e){e.preventDefault(),alert(JSON.stringify(this.form))},onReset(e){e.preventDefault(),this.form.email="",this.form.name="",this.form.food=null,this.form.checked=[],this.show=!1,this.$nextTick((()=>{this.show=!0}))}}};const S=(0,i.Z)(y,[["render",w]]);var k=S,O=a(7139);const W=e=>((0,o.dD)("data-v-5e99c624"),e=e(),(0,o.Cn)(),e),j={class:"e0_3"},R=W((()=>(0,o._)("h5",{class:"card-title"},"Валидация сертификата",-1))),V=(0,o.Uk)("Валидировать!"),D=(0,o.Uk)("Загрузить файл"),T={class:"m-0"},U=(0,o.uE)('<div class="e33_53" data-v-5e99c624><div class="e4_7" data-v-5e99c624></div><span class="e4_8" data-v-5e99c624>ИНФРАСТРУКТУРА ДОВЕРИЯ</span><span class="e4_9" data-v-5e99c624>О РОСАККРЕДИТАЦИИ</span><span class="e4_10" data-v-5e99c624>НИАР</span><span class="e4_11" data-v-5e99c624>ТЕХНОЛОГИЧНОСТЬ</span><span class="e4_12" data-v-5e99c624>КОМПЕТЕНТНОСТЬ</span><span class="e4_13" data-v-5e99c624>ПРЕСС-ЦЕНТР</span><span class="e4_14" data-v-5e99c624>ДОКУМЕНТЫ</span><span class="e4_15" data-v-5e99c624>ОБРАТНАЯ СВЯЗЬ</span></div><div class="e33_48" data-v-5e99c624><div class="e4_2" data-v-5e99c624></div></div><div class="e33_46" data-v-5e99c624><div class="e4_4" data-v-5e99c624></div></div><div class="e33_47" data-v-5e99c624><div class="e4_3" data-v-5e99c624></div></div><div class="e33_45" data-v-5e99c624><div class="e4_5" data-v-5e99c624></div></div>',5);function C(e,t,a,n,r,l){const i=(0,o.up)("b-form-input"),s=(0,o.up)("b-form-group"),u=(0,o.up)("b-button"),d=(0,o.up)("b-form"),c=(0,o.up)("b-card"),p=(0,o.up)("b-container");return(0,o.wg)(),(0,o.iD)("div",j,[(0,o.Wm)(p,{class:"task1-form"},{default:(0,o.w5)((()=>[(0,o.Wm)(c,null,{default:(0,o.w5)((()=>[R,(0,o.Wm)(d,{onSubmit:l.onSubmit,onReset:l.onReset},{default:(0,o.w5)((()=>[(0,o.Wm)(s,{id:"input-group-1",label:"Коды ТН ВЭД ЕАЭС","label-for":"input-1"},{default:(0,o.w5)((()=>[(0,o.Wm)(i,{id:"input-1",modelValue:r.form1.tnved,"onUpdate:modelValue":t[0]||(t[0]=e=>r.form1.tnved=e),placeholder:"",required:""},null,8,["modelValue"])])),_:1}),(0,o.Wm)(s,{id:"input-group-2",label:"Технические регламенты","label-for":"input-2"},{default:(0,o.w5)((()=>[(0,o.Wm)(i,{id:"input-2",modelValue:r.form1.reglament,"onUpdate:modelValue":t[1]||(t[1]=e=>r.form1.reglament=e),placeholder:"",required:""},null,8,["modelValue"])])),_:1}),(0,o.Wm)(s,{id:"input-group-3",label:"Группа продукции","label-for":"input-3"},{default:(0,o.w5)((()=>[(0,o.Wm)(i,{id:"input-3",modelValue:r.form1.group,"onUpdate:modelValue":t[2]||(t[2]=e=>r.form1.group=e),placeholder:"",required:""},null,8,["modelValue"])])),_:1}),(0,o.Wm)(s,{id:"input-group-4",label:"Наименование продукции","label-for":"input-4"},{default:(0,o.w5)((()=>[(0,o.Wm)(i,{id:"input-4",modelValue:r.form1.productName,"onUpdate:modelValue":t[3]||(t[3]=e=>r.form1.productName=e),placeholder:"",required:""},null,8,["modelValue"])])),_:1}),(0,o.Wm)(u,{class:"form-button",type:"submit",variant:"primary"},{default:(0,o.w5)((()=>[V])),_:1}),(0,o.Wm)(u,{class:"form-button",type:"reset",variant:"primary"},{default:(0,o.w5)((()=>[D])),_:1})])),_:1},8,["onSubmit","onReset"]),r.show?((0,o.wg)(),(0,o.j4)(c,{key:0,class:"mt-3",header:"Form Data Result"},{default:(0,o.w5)((()=>[(0,o._)("pre",T,(0,O.zw)(r.task1_answer),1)])),_:1})):(0,o.kq)("",!0)])),_:1})])),_:1}),U])}var x={name:"indexOne",data(){return{form1:{tnved:"",reglament:"",group:"",productName:""},show:!1,task1_answer:{validation_score:100}}},methods:{onSubmit(e){e.preventDefault();let t=JSON.stringify(this.form);h().defaults.headers.post["Content-Type"]="application/json;charset=utf-8",h().defaults.headers.post["Access-Control-Allow-Origin"]="*",h().post("/api/task1_form",t).then((e=>()=>{console.log(e),this.task1_answer=e.data,this.show=!0}))},onReset(e){e.preventDefault()}}};const E=(0,i.Z)(x,[["render",C],["__scopeId","data-v-5e99c624"]]);var F=E,P=a(2483),N=a(936);const q=(0,n.ri)(u),A=a(4855);q.use(A,d),q.use(N.ZP);const I=[{path:"/",component:F},{path:"/task1",component:g},{path:"/task2",component:k}],Z=(0,P.p7)({history:(0,P.r5)(),routes:I});q.use(Z),q.mount("#app")}},t={};function a(n){var o=t[n];if(void 0!==o)return o.exports;var r=t[n]={exports:{}};return e[n].call(r.exports,r,r.exports,a),r.exports}a.m=e,function(){var e=[];a.O=function(t,n,o,r){if(!n){var l=1/0;for(d=0;d<e.length;d++){n=e[d][0],o=e[d][1],r=e[d][2];for(var i=!0,s=0;s<n.length;s++)(!1&r||l>=r)&&Object.keys(a.O).every((function(e){return a.O[e](n[s])}))?n.splice(s--,1):(i=!1,r<l&&(l=r));if(i){e.splice(d--,1);var u=o();void 0!==u&&(t=u)}}return t}r=r||0;for(var d=e.length;d>0&&e[d-1][2]>r;d--)e[d]=e[d-1];e[d]=[n,o,r]}}(),function(){a.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return a.d(t,{a:t}),t}}(),function(){a.d=function(e,t){for(var n in t)a.o(t,n)&&!a.o(e,n)&&Object.defineProperty(e,n,{enumerable:!0,get:t[n]})}}(),function(){a.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){a.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)}}(),function(){a.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})}}(),function(){var e={143:0};a.O.j=function(t){return 0===e[t]};var t=function(t,n){var o,r,l=n[0],i=n[1],s=n[2],u=0;if(l.some((function(t){return 0!==e[t]}))){for(o in i)a.o(i,o)&&(a.m[o]=i[o]);if(s)var d=s(a)}for(t&&t(n);u<l.length;u++)r=l[u],a.o(e,r)&&e[r]&&e[r][0](),e[r]=0;return a.O(d)},n=self["webpackChunkapollo_front"]=self["webpackChunkapollo_front"]||[];n.forEach(t.bind(null,0)),n.push=t.bind(null,n.push.bind(n))}();var n=a.O(void 0,[998],(function(){return a(4354)}));n=a.O(n)})();
//# sourceMappingURL=app.e5f8eb05.js.map