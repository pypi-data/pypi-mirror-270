import{d as y,r as v,K as A,o as V,eO as f,b as u,c,w as o,f as t,u as e,as as h,cC as x,e as s,eH as _,bA as C}from"./outputWidgets.c7d11ead.js";import{d as D}from"./vuedraggable.umd.09215b20.js";import{_ as S}from"./SaveButton.vue_vue_type_script_setup_true_lang.9810d90c.js";import{A as I}from"./Item.4cc2b8d8.js";import{A as L}from"./index.ed42937c.js";import{A as w}from"./Title.fdf5c01d.js";import{A as g}from"./index.8343729f.js";import{A as b}from"./index.bcace449.js";import{A as E,F}from"./Form.894c92e7.js";import{S as U}from"./SidebarPreview.89f86e1c.js";import{C as $}from"./ContentLayout.081ded6d.js";import{L as B}from"./LoadingContainer.9fd2b01d.js";import{a as N}from"./asyncComputed.0d9bf0ef.js";import{W as T}from"./workspaces.56466063.js";import"./envVars.76285d02.js";import"./UnsavedChangesHandler.97f6b632.js";import"./ExclamationCircleOutlined.276cec24.js";import"./Modal.7ab5d69d.js";import"./Base.984b27ce.js";import"./Link.38c2ac16.js";import"./hasIn.dd565870.js";import"./PlayerNavbar.bdbf5c9a.js";import"./PhKanban.vue.a22767a3.js";import"./PhSignOut.vue.66a76268.js";import"./Text.eba38ee8.js";import"./index.b96c4fab.js";import"./Paragraph.a2d4bb5b.js";import"./index.8e44e8fb.js";import"./WidgetsFrame.52136fe3.js";import"./runnerData.0f2179f9.js";import"./url.20f0444a.js";import"./HomeContent.858c262b.js";import"./PhArrowSquareOut.vue.4830520f.js";import"./index.eb1f7996.js";import"./Card.f339dcbe.js";import"./TabPane.4688ff0a.js";import"./record.e5cfb835.js";import"./pubsub.a91a3d3f.js";(function(){try{var r=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},a=new Error().stack;a&&(r._sentryDebugIds=r._sentryDebugIds||{},r._sentryDebugIds[a]="189b36f1-8c12-4fe3-8429-4d7962372d0e",r._sentryDebugIdIdentifier="sentry-dbid-189b36f1-8c12-4fe3-8429-4d7962372d0e")}catch{}})();const j=s("span",null,"Route",-1),M=s("span",null,"Title",-1),R=s("span",null,"Visible",-1),W={style:{flex:"1 0"}},q={style:{flex:"1 0"}},z=y({__name:"SidebarEditor",props:{modelValue:{},workspace:{}},emits:["update:modelValue"],setup(r,{emit:a}){const n=r,i=v([]),p=()=>a("update:modelValue",i.value);return A(()=>n.modelValue,(d,m)=>{f.exports.isEqual(d,m)||(i.value=f.exports.cloneDeep(d))}),V(()=>{i.value=f.exports.cloneDeep(n.modelValue)}),(d,m)=>(u(),c(e(E),{help:"Change your sidebar items position and visibility by dragging them up and down"},{default:o(()=>[t(e(g),{justify:"space-between",style:{margin:"0 0 12px 0"}},{default:o(()=>[t(e(w),{level:4,style:{margin:"0"}},{default:o(()=>[h("Sidebar items")]),_:1}),t(S,{model:d.workspace},null,8,["model"])]),_:1}),t(e(L),{bordered:""},{header:o(()=>[t(e(x),{style:{width:"100%","justify-content":"space-between"}},{default:o(()=>[j,t(e(b),{type:"vertical"}),M,t(e(b),{type:"vertical"}),R]),_:1})]),default:o(()=>[t(e(D),{modelValue:i.value,"onUpdate:modelValue":m[0]||(m[0]=l=>i.value=l),style:{width:"100%"},onChange:p},{item:o(({element:l})=>[t(e(I),{style:{cursor:"ns-resize"}},{default:o(()=>[s("span",W,"/"+_(l.path),1),s("span",q,_(l.name),1),t(e(C),{checked:l.visible,"onUpdate:checked":k=>l.visible=k,type:"checkbox",onChange:p},null,8,["checked","onUpdate:checked"])]),_:2},1024)]),_:1},8,["modelValue"])]),_:1})]),_:1}))}}),H={style:{width:"50%"}},K={style:{width:"50%"}},Le=y({__name:"SidebarEditor",setup(r){const{result:a,loading:n}=N(()=>T.get());return(i,p)=>(u(),c($,null,{default:o(()=>[e(n)||!e(a)?(u(),c(B,{key:0})):(u(),c(e(F),{key:1,style:{width:"100%"}},{default:o(()=>[t(e(w),null,{default:o(()=>[h("Sidebar")]),_:1}),t(e(g),{gap:"40"},{default:o(()=>[s("div",H,[t(z,{modelValue:e(a).sidebar,"onUpdate:modelValue":p[0]||(p[0]=d=>e(a).sidebar=d),workspace:e(a)},null,8,["modelValue","workspace"])]),s("div",K,[t(U,{workspace:e(a),"widgets-visible":!1},null,8,["workspace"])])]),_:1})]),_:1}))]),_:1}))}});export{Le as default};
//# sourceMappingURL=SidebarEditor.6a35018d.js.map
