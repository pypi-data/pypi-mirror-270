import{i as y}from"./url.20f0444a.js";import"./outputWidgets.c7d11ead.js";(function(){try{var e=typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},a=new Error().stack;a&&(e._sentryDebugIds=e._sentryDebugIds||{},e._sentryDebugIds[a]="32ef971f-786d-4bdf-916e-6051d3842ae8",e._sentryDebugIdIdentifier="sentry-dbid-32ef971f-786d-4bdf-916e-6051d3842ae8")}catch{}})();function D(e,a,r){return a?y(a)?a:r==="player"?`/_assets/${e}`:`/_editor/api/assets/${a}`:null}const g="#414a58",w="#FFFFFF",T="#000000",F="DM Sans",O="Untitled Project";function M(e){var a,r,t,s,n,l,o,u,_,i,f,m,c,b,p;return{id:e.id,path:e.path,theme:(a=e.workspace.theme)!=null?a:w,brandName:(r=e.workspace.brand_name)!=null?r:null,title:e.title,isLocal:(t=e.is_local)!=null?t:!1,startMessage:(s=e.start_message)!=null?s:null,endMessage:(n=e.end_message)!=null?n:null,errorMessage:(l=e.error_message)!=null?l:null,timeoutMessage:(o=e.timeout_message)!=null?o:null,startButtonText:(u=e.start_button_text)!=null?u:null,restartButtonText:(_=e.restart_button_text)!=null?_:null,logoUrl:e.workspace.logo_url,mainColor:(i=e.workspace.main_color)!=null?i:g,fontFamily:(f=e.workspace.font_family)!=null?f:F,autoStart:(m=e.auto_start)!=null?m:!1,allowRestart:e.allow_restart,welcomeTitle:(c=e.welcome_title)!=null?c:null,runtimeType:"form",sidebar:(p=(b=e.workspace)==null?void 0:b.sidebar)!=null?p:[]}}function d(e){return{name:e.name||O,fontColor:e.font_color||T,sidebar:e.sidebar||[],brandName:e.brand_name||"",fontFamily:e.font_family||F,logoUrl:e.logo_url?D("logo",e.logo_url,"player"):null,mainColor:e.main_color||g,theme:e.theme||w}}export{g as D,F as a,w as b,D as m,M as r,d as w};
//# sourceMappingURL=runnerData.0f2179f9.js.map
