(this.webpackJsonpui_v2=this.webpackJsonpui_v2||[]).push([[20],{1313:function(n,t,e){},1316:function(n,t,e){"use strict";e.r(t),e.d(t,"LogsLastRequestEnum",(function(){return _}));var r=e(7),u=e(0),i=e.n(u),o=e(72),a=e(267),l=e(18),c=e.n(l),s=e(279),d=e(280),f=e(11),v=e(370),b=e(5),g=e(17),p=e(63),h=e(843),m=e(14),x=e(9),j={fg:"#FFF",bg:"#000",newline:!1,colors:function(){var n={0:"#000",1:"#A00",2:"#0A0",3:"#A50",4:"#00A",5:"#A0A",6:"#0AA",7:"#AAA",8:"#555",9:"#F55",10:"#5F5",11:"#FF5",12:"#55F",13:"#F5F",14:"#5FF",15:"#FFF"};return o.a.range(0,6).forEach((function(t){o.a.range(0,6).forEach((function(e){o.a.range(0,6).forEach((function(r){return function(n,t,e,r){var u=n>0?40*n+55:0,i=t>0?40*t+55:0,o=e>0?40*e+55:0;r[16+36*n+6*t+e]=function(n){var t,e=[],r=Object(x.a)(n);try{for(r.s();!(t=r.n()).done;){var u=t.value;e.push(L(u))}}catch(i){r.e(i)}finally{r.f()}return"#"+e.join("")}([u,i,o])}(t,e,r,n)}))}))})),o.a.range(0,24).forEach((function(t){var e=t+232,r=L(10*t+8);n[e]="#"+r+r+r})),n}()};function L(n){for(var t=n.toString(16);t.length<2;)t="0"+t;return t}function O(n,t,e,r){var u;if("text"===t)u=e;else if("display"===t)u=function(n,t,e){t=parseInt("".concat(t),10);var r={"-1":function(){return"<br/>"},0:function(){return n.length&&E(n)},1:function(){return A(n,"b")},3:function(){return A(n,"i")},4:function(){return A(n,"u")},8:function(){return y(n,"display:none")},9:function(){return A(n,"strike")},22:function(){return y(n,"font-weight:normal;text-decoration:none;font-style:normal")},23:function(){return T(n,"i")},24:function(){return T(n,"u")},39:function(){return I(n,e.fg)},49:function(){return F(n,e.bg)},53:function(){return y(n,"text-decoration:overline")}};if(r[t])return r[t]();if(4<t&&t<7)return A(n,"blink");var u,i,o,a;if(29<t&&t<38)return I(n,null===e||void 0===e||null===(u=e.colors)||void 0===u?void 0:u[t-30]);if(39<t&&t<48)return F(n,null===e||void 0===e||null===(i=e.colors)||void 0===i?void 0:i[t-40]);if(89<t&&t<98)return I(n,null===e||void 0===e||null===(o=e.colors)||void 0===o?void 0:o[t-90+8]);if(99<t&&t<108)return F(n,null===e||void 0===e||null===(a=e.colors)||void 0===a?void 0:a[t-100+8])}(n,+e,r);else if("xterm256Foreground"===t){var i;u=I(n,null===r||void 0===r||null===(i=r.colors)||void 0===i?void 0:i[+e])}else if("xterm256Background"===t){var o;u=F(n,null===r||void 0===r||null===(o=r.colors)||void 0===o?void 0:o[+e])}else"rgb"===t&&(u=function(n,t){var e=+(t=t.substring(2).slice(0,-1)).substr(0,2),r=t.substring(5).split(";").map((function(n){return("0"+Number(n).toString(16)).substring(-2)})).join("");return y(n,(38===e?"color:#":"background-color:#")+r)}(n,e));return u}function E(n){var t=n.slice(0);return n.length=0,t.reverse().map((function(n){return"</"+n+">"})).join("")}function A(n,t,e){return e||(e=""),n.push(t),"<".concat(t).concat(e?' style="'.concat(e,'"'):"",">")}function y(n,t){return A(n,"span",t)}function I(n,t){return A(n,"span","color:"+t)}function F(n,t){return A(n,"span","background-color:"+t)}function T(n,t){var e;if(n.slice(-1)[0]===t&&(e=n.pop()),e)return"</"+t+">"}var D=function(n,t){n="string"===typeof n?[n]:n;var e=Object.assign({},j,t),r=[],u=[];return function(n,t,e){var r=!1;function u(){return""}function i(n){return t.newline?e("display",-1):e("text",n),""}var o=[{pattern:/^\x08+/,sub:u},{pattern:/^\x1b\[[012]?K/,sub:u},{pattern:/^\x1b\[\(B/,sub:u},{pattern:/^\x1b\[[34]8;2;\d+;\d+;\d+m/,sub:function(n){return e("rgb",n),""}},{pattern:/^\x1b\[38;5;(\d+)m/,sub:function(n,t){return e("xterm256Foreground",t),""}},{pattern:/^\x1b\[48;5;(\d+)m/,sub:function(n,t){return e("xterm256Background",t),""}},{pattern:/^\n/,sub:i},{pattern:/^\r+\n/,sub:i},{pattern:/^\r/,sub:i},{pattern:/^\x1b\[((?:\d{1,3};?)+|)m/,sub:function(n,t){r=!0,0===t.trim().length&&(t="0");var u,i=t.trimRight().split(";"),o=Object(x.a)(i);try{for(o.s();!(u=o.n()).done;){var a=u.value;e("display",a)}}catch(l){o.e(l)}finally{o.f()}return""}},{pattern:/^\x1b\[\d?J/,sub:u},{pattern:/^\x1b\[\d{0,3};\d{0,3}f/,sub:u},{pattern:/^\x1b\[?[\d;]{0,3}/,sub:u},{pattern:/^(([^\x1b\x08\r\n])+)/,sub:function(n){return e("text",n),""}}];function a(t,e){e>3&&r||(r=!1,n=n.replace(t.pattern,t.sub))}var l=[],c=n.length;n:for(;c>0;){for(var s=0,d=0,f=o.length;d<f;s=++d)if(a(o[s],s),n.length!==c){c=n.length;continue n}if(n.length===c)break;l.push(0),c=n.length}}(n.join(""),e,(function(n,t){var i=O(r,n,"".concat(t),e);i&&u.push(i)})),r.length&&u.push(E(r)),u.join("")},R=e(1);function S(n){var t,e,r=n.index,u=n.style,i=n.data;return Object(R.jsx)("div",{style:u,children:Object(R.jsx)("pre",{className:"LogRow__line",dangerouslySetInnerHTML:{__html:D(null!==(t=null===(e=i.logsList)||void 0===e?void 0:e[r-1])&&void 0!==t?t:"")}})})}S.displayName="RunLogsTab";var _,k=i.a.memo(S);!function(n){n.DEFAULT="default",n.LIVE_UPDATE="live-update",n.LOAD_MORE="load-more"}(_||(_={}));e(1313);function N(n){var t,e,u=n.isRunLogsLoading,l=n.runHash,x=n.runLogs,j=n.inProgress,L=n.updatedLogsCount,O=i.a.useRef(null),E=i.a.useRef(null),A=i.a.useRef({}),y=i.a.useRef({}),I=i.a.useRef(null),F=i.a.useState(_.DEFAULT),T=Object(r.a)(F,2),D=T[0],S=T[1],N=i.a.useState(p.a.Ok),w=Object(r.a)(N,2),U=w[0],P=w[1],H=i.a.useRef([0,0]),V=i.a.useState(null),B=Object(r.a)(V,2),M=B[0],z=B[1],C=i.a.useState(null),J=Object(r.a)(C,2),W=J[0],q=J[1],K=i.a.useState(0),G=Object(r.a)(K,2),Q=G[0],X=G[1],Y=i.a.useState(0),Z=Object(r.a)(Y,2),$=Z[0],nn=Z[1],tn=i.a.useState(null),en=Object(r.a)(tn,2),rn=en[0],un=en[1];function on(){var n,t;S(_.LIVE_UPDATE),an({runHash:l,record_range:I.current?"".concat((null===(n=H.current)||void 0===n?void 0:n[1])>5?(null===(t=H.current)||void 0===t?void 0:t[1])-5:0,":"):""})}function an(n){P(p.a.Pending),y.current=h.a.getRunLogs(n),y.current.call().then((function(){P(p.a.Ok),ln(),function(){if(j){var n=window.setTimeout(on,3e3);O.current={intervalId:n}}}()}))}function ln(){var n,t,e=arguments.length>0&&void 0!==arguments[0]&&arguments[0];(e||D===_.LIVE_UPDATE)&&(null===(t=y.current)||void 0===t||t.abort());(null===(n=O.current)||void 0===n?void 0:n.intervalId)&&clearInterval(O.current.intervalId)}return i.a.useEffect((function(){return an({runHash:l}),m.a(g.a.runDetails.tabs.logs.tabView),function(){ln(!0)}}),[]),i.a.useEffect((function(){j||ln()}),[j]),i.a.useEffect((function(){var n=o.a.sortBy(Object.values(null!==x&&void 0!==x?x:{}),"index"),t=o.a.sortBy(n.map((function(n){return+n.index}))),e=Array(3).fill("");H.current=[t[0],t[t.length-1]],un(t),I.current=n.map((function(n){return n.value})).concat(e)}),[x]),i.a.useEffect((function(){var n,t,e,r,u=null!==(n=null===(t=I.current)||void 0===t?void 0:t.length)&&void 0!==n?n:0;if(D===_.LOAD_MORE&&W)null===(e=A.current)||void 0===e||null===(r=e.scrollToItem)||void 0===r||r.call(e,W.visibleStartIndex+L,"start"),S(_.DEFAULT);else if(D===_.LIVE_UPDATE&&W&&(null===W||void 0===W?void 0:W.visibleStopIndex)+L>=u-1||D===_.DEFAULT){var i,a;if(!o.a.isEmpty(rn))null===(i=A.current)||void 0===i||null===(a=i.scrollToItem)||void 0===a||a.call(i,u,"end")}else{var l,c,s;null===(l=A.current)||void 0===l||null===(c=l.scrollToItem)||void 0===c||c.call(l,null!==(s=null===W||void 0===W?void 0:W.visibleStartIndex)&&void 0!==s?s:0,"start")}}),[I.current,rn]),i.a.useEffect((function(){var n,t,e;D===_.DEFAULT&&Q&&$&&(o.a.isEmpty(rn)||null===(n=A.current)||void 0===n||null===(t=n.scrollToItem)||void 0===t||t.call(n,null!==(e=null===W||void 0===W?void 0:W.visibleStartIndex)&&void 0!==e?e:0,"start"))}),[Q,$]),Object(s.c)((function(){E.current&&(X(E.current.offsetHeight),nn(E.current.offsetWidth))}),E),Object(R.jsx)(f.a,{children:Object(R.jsx)(d.a,{isLoading:u&&D===_.DEFAULT,className:"RunDetailTabLoader",height:"100%",children:o.a.isEmpty(x)||o.a.isEmpty(rn)||o.a.isNil(I.current)?Object(R.jsx)(v.a,{size:"xLarge",className:"RunDetailTabLoader",title:"No Logs"}):Object(R.jsx)("div",{className:"RunDetailLogsTabWrapper",children:Object(R.jsx)("div",{className:"RunDetailLogsTab",children:Object(R.jsx)("div",{className:"Logs",ref:E,children:Object(R.jsxs)("div",{className:"Logs__wrapper",children:[Object(R.jsx)(a.d,{ref:A,height:Q||100,itemCount:(null===(t=I.current)||void 0===t?void 0:t.length)+1,itemSize:function(){return 15},width:"100%",overscanCount:100,initialScrollOffset:null!==M&&void 0!==M?M:15*(null===(e=I.current)||void 0===e?void 0:e.length),onItemsRendered:function(n){var t=n.visibleStartIndex,e=n.visibleStopIndex;q({visibleStartIndex:t,visibleStopIndex:e})},itemData:{logsList:I.current},onScroll:function(n){var t,e,r,u=n.scrollOffset,i=n.scrollDirection;z(u),u<=15&&rn&&0!==rn[0]&&"backward"===i&&(U===p.a.Ok||U===p.a.Pending&&D===_.LIVE_UPDATE)&&(ln(),S(_.LOAD_MORE),an({runHash:l,record_range:"".concat((null===(t=H.current)||void 0===t?void 0:t[0])>200?(null===(e=H.current)||void 0===e?void 0:e[0])-200:0,":").concat(null===(r=H.current)||void 0===r?void 0:r[0])}))},children:k},"".concat(Q).concat($)),Object(R.jsx)("div",{className:c()("overlay",{loading:u&&D===_.LOAD_MORE}),children:Object(R.jsx)(b.l,{size:24})})]})})})})})})}N.displayName="RunLogsTab";var w=i.a.memo(N);t.default=w}}]);
//# sourceMappingURL=RunLogsTab.js.map?version=7f6f605f2ee17125599e