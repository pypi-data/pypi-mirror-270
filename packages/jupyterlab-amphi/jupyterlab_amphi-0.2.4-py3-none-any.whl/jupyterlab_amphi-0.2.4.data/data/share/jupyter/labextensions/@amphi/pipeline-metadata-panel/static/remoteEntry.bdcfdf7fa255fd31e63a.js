var _JUPYTERLAB;(()=>{"use strict";var e,r,t,a,n,i,o,l,u,p,d,f,s,c,h,v,m,g={320:(e,r,t)=>{var a={"./index":()=>t.e(732).then((()=>()=>t(732))),"./extension":()=>t.e(732).then((()=>()=>t(732))),"./style":()=>t.e(432).then((()=>()=>t(432)))},n=(e,r)=>(t.R=r,r=t.o(a,e)?a[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),i=(e,r)=>{if(t.S){var a="default",n=t.S[a];if(n&&n!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[a]=e,t.I(a,r)}};t.d(r,{get:()=>n,init:()=>i})}},b={};function y(e){var r=b[e];if(void 0!==r)return r.exports;var t=b[e]={id:e,exports:{}};return g[e](t,t.exports,y),t.exports}y.m=g,y.c=b,y.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return y.d(r,{a:r}),r},y.d=(e,r)=>{for(var t in r)y.o(r,t)&&!y.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},y.f={},y.e=e=>Promise.all(Object.keys(y.f).reduce(((r,t)=>(y.f[t](e,r),r)),[])),y.u=e=>e+"."+{432:"1dff82965ae8eeafd45c",732:"5ee1843a7c6f18d4f9f9"}[e]+".js?v="+{432:"1dff82965ae8eeafd45c",732:"5ee1843a7c6f18d4f9f9"}[e],y.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),y.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),e={},r="@amphi/pipeline-metadata-panel:",y.l=(t,a,n,i)=>{if(e[t])e[t].push(a);else{var o,l;if(void 0!==n)for(var u=document.getElementsByTagName("script"),p=0;p<u.length;p++){var d=u[p];if(d.getAttribute("src")==t||d.getAttribute("data-webpack")==r+n){o=d;break}}o||(l=!0,(o=document.createElement("script")).charset="utf-8",o.timeout=120,y.nc&&o.setAttribute("nonce",y.nc),o.setAttribute("data-webpack",r+n),o.src=t),e[t]=[a];var f=(r,a)=>{o.onerror=o.onload=null,clearTimeout(s);var n=e[t];if(delete e[t],o.parentNode&&o.parentNode.removeChild(o),n&&n.forEach((e=>e(a))),r)return r(a)},s=setTimeout(f.bind(null,void 0,{type:"timeout",target:o}),12e4);o.onerror=f.bind(null,o.onerror),o.onload=f.bind(null,o.onload),l&&document.head.appendChild(o)}},y.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},(()=>{y.S={};var e={},r={};y.I=(t,a)=>{a||(a=[]);var n=r[t];if(n||(n=r[t]={}),!(a.indexOf(n)>=0)){if(a.push(n),e[t])return e[t];y.o(y.S,t)||(y.S[t]={});var i=y.S[t],o="@amphi/pipeline-metadata-panel",l=[];return"default"===t&&((e,r,t,a)=>{var n=i[e]=i[e]||{},l=n[r];(!l||!l.loaded&&(1!=!l.eager?a:o>l.from))&&(n[r]={get:()=>y.e(732).then((()=>()=>y(732))),from:o,eager:!1})})("@amphi/pipeline-metadata-panel","0.2.4"),e[t]=l.length?Promise.all(l).then((()=>e[t]=1)):1}}})(),(()=>{var e;y.g.importScripts&&(e=y.g.location+"");var r=y.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");if(t.length)for(var a=t.length-1;a>-1&&(!e||!/^http(s?):/.test(e));)e=t[a--].src}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),y.p=e})(),t=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),a=t[1]?r(t[1]):[];return t[2]&&(a.length++,a.push.apply(a,r(t[2]))),t[3]&&(a.push([]),a.push.apply(a,r(t[3]))),a},a=(e,r)=>{e=t(e),r=t(r);for(var a=0;;){if(a>=e.length)return a<r.length&&"u"!=(typeof r[a])[0];var n=e[a],i=(typeof n)[0];if(a>=r.length)return"u"==i;var o=r[a],l=(typeof o)[0];if(i!=l)return"o"==i&&"n"==l||"s"==l||"u"==i;if("o"!=i&&"u"!=i&&n!=o)return n<o;a++}},n=e=>{var r=e[0],t="";if(1===e.length)return"*";if(r+.5){t+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var a=1,i=1;i<e.length;i++)a--,t+="u"==(typeof(l=e[i]))[0]?"-":(a>0?".":"")+(a=2,l);return t}var o=[];for(i=1;i<e.length;i++){var l=e[i];o.push(0===l?"not("+u()+")":1===l?"("+u()+" || "+u()+")":2===l?o.pop()+" "+o.pop():n(l))}return u();function u(){return o.pop().replace(/^\((.+)\)$/,"$1")}},i=(e,r)=>{if(0 in e){r=t(r);var a=e[0],n=a<0;n&&(a=-a-1);for(var o=0,l=1,u=!0;;l++,o++){var p,d,f=l<e.length?(typeof e[l])[0]:"";if(o>=r.length||"o"==(d=(typeof(p=r[o]))[0]))return!u||("u"==f?l>a&&!n:""==f!=n);if("u"==d){if(!u||"u"!=f)return!1}else if(u)if(f==d)if(l<=a){if(p!=e[l])return!1}else{if(n?p>e[l]:p<e[l])return!1;p!=e[l]&&(u=!1)}else if("s"!=f&&"n"!=f){if(n||l<=a)return!1;u=!1,l--}else{if(l<=a||d<f!=n)return!1;u=!1}else"s"!=f&&"n"!=f&&(u=!1,l--)}}var s=[],c=s.pop.bind(s);for(o=1;o<e.length;o++){var h=e[o];s.push(1==h?c()|c():2==h?c()&c():h?i(h,r):!c())}return!!c()},o=(e,r)=>{var t=y.S[e];if(!t||!y.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},l=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&a(e,r)?r:e),0)},u=(e,r,t,a)=>"Unsatisfied version "+t+" from "+(t&&e[r][t].from)+" of shared singleton module "+r+" (required "+n(a)+")",p=(e,r,t,a)=>{var n=l(e,t);return i(a,n)||d(u(e,t,n,a)),f(e[t][n])},d=e=>{"undefined"!=typeof console&&console.warn&&console.warn(e)},f=e=>(e.loaded=1,e.get()),s=(e=>function(r,t,a,n){var i=y.I(r);return i&&i.then?i.then(e.bind(e,r,y.S[r],t,a,n)):e(r,y.S[r],t,a)})(((e,r,t,a)=>(o(e,t),p(r,0,t,a)))),c={},h={44:()=>s("default","@jupyterlab/console",[1,4,1,6]),88:()=>s("default","@lumino/datagrid",[1,2,3,0,,"alpha",0]),256:()=>s("default","@lumino/widgets",[1,2,3,1,,"alpha",0]),262:()=>s("default","@lumino/coreutils",[1,2,0,0]),465:()=>s("default","@jupyterlab/application",[1,4,1,6]),602:()=>s("default","@lumino/signaling",[1,2,0,0]),638:()=>s("default","@jupyterlab/apputils",[1,4,2,6]),664:()=>s("default","@jupyterlab/ui-components",[1,4,1,6]),881:()=>s("default","@amphi/pipeline-editor",[0])},v={732:[44,88,256,262,465,602,638,664,881]},m={},y.f.consumes=(e,r)=>{y.o(v,e)&&v[e].forEach((e=>{if(y.o(c,e))return r.push(c[e]);if(!m[e]){var t=r=>{c[e]=0,y.m[e]=t=>{delete y.c[e],t.exports=r()}};m[e]=!0;var a=r=>{delete c[e],y.m[e]=t=>{throw delete y.c[e],r}};try{var n=h[e]();n.then?r.push(c[e]=n.then(t).catch(a)):t(n)}catch(e){a(e)}}}))},(()=>{var e={680:0};y.f.j=(r,t)=>{var a=y.o(e,r)?e[r]:void 0;if(0!==a)if(a)t.push(a[2]);else{var n=new Promise(((t,n)=>a=e[r]=[t,n]));t.push(a[2]=n);var i=y.p+y.u(r),o=new Error;y.l(i,(t=>{if(y.o(e,r)&&(0!==(a=e[r])&&(e[r]=void 0),a)){var n=t&&("load"===t.type?"missing":t.type),i=t&&t.target&&t.target.src;o.message="Loading chunk "+r+" failed.\n("+n+": "+i+")",o.name="ChunkLoadError",o.type=n,o.request=i,a[1](o)}}),"chunk-"+r,r)}};var r=(r,t)=>{var a,n,[i,o,l]=t,u=0;if(i.some((r=>0!==e[r]))){for(a in o)y.o(o,a)&&(y.m[a]=o[a]);l&&l(y)}for(r&&r(t);u<i.length;u++)n=i[u],y.o(e,n)&&e[n]&&e[n][0](),e[n]=0},t=self.webpackChunk_amphi_pipeline_metadata_panel=self.webpackChunk_amphi_pipeline_metadata_panel||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})(),y.nc=void 0;var w=y(320);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["@amphi/pipeline-metadata-panel"]=w})();