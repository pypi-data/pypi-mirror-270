import{d as g,eK as b,r as y,K as h,b as v,ew as w,f as m,u as a,x as k}from"./outputWidgets.c7d11ead.js";import{g as H}from"./api.c8e1b94a.js";import{a as p}from"./asyncComputed.0d9bf0ef.js";import{P as I}from"./PlayerNavbar.bdbf5c9a.js";import{H as x}from"./HomeContent.858c262b.js";import{u as s}from"./index.5ad1e225.js";import"./runnerData.0f2179f9.js";import"./url.20f0444a.js";import"./PhKanban.vue.a22767a3.js";import"./PhSignOut.vue.66a76268.js";import"./Text.eba38ee8.js";import"./Base.984b27ce.js";import"./index.b96c4fab.js";import"./Link.38c2ac16.js";import"./Paragraph.a2d4bb5b.js";import"./Title.fdf5c01d.js";import"./index.8e44e8fb.js";import"./PhArrowSquareOut.vue.4830520f.js";import"./index.eb1f7996.js";import"./Card.f339dcbe.js";import"./TabPane.4688ff0a.js";import"./hasIn.dd565870.js";import"./index.8343729f.js";import"./fetch.9493b87c.js";import"./pubsub.a91a3d3f.js";(function(){try{var o=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},e=new Error().stack;e&&(o._sentryDebugIds=o._sentryDebugIds||{},o._sentryDebugIds[e]="047284e8-62e5-401a-9c6a-42d07dd1cec5",o._sentryDebugIdIdentifier="sentry-dbid-047284e8-62e5-401a-9c6a-42d07dd1cec5")}catch{}})();const D={class:"page"},C=g({__name:"Home",setup(o){const e=b(),r=y(s.getUser()),{result:c,refetch:u}=p(async()=>(await s.allow("kanban")).status==="ALLOWED");h(r,()=>u());const d=({path:t})=>{e.push({name:"form",params:{path:t.split("/")}})},{result:n,loading:l}=p(H),f=t=>{e.push({path:`/${t}`})},_=()=>{s.removeUser(),e.push({name:"playerHome"})};return(t,K)=>{var i;return v(),w("div",D,[m(I,{"runner-data":a(n),"is-kanban-visible":a(c)||!1,"user-email":(i=r.value)==null?void 0:i.claims.email,onNavigate:d,onLogout:_},null,8,["runner-data","is-kanban-visible","user-email"]),m(x,{workspace:a(n),loading:a(l),onFormClick:f},null,8,["workspace","loading"])])}}});const ee=k(C,[["__scopeId","data-v-f12c98c4"]]);export{ee as default};
//# sourceMappingURL=Home.743285c5.js.map
