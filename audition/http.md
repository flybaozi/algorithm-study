`
浏览器输入URL地址到呈现页面给用户，中间到底发生了什么?用到了什么协议。
`

`
DNS的查找过程是这样的：
`

`
chrome浏览器会先查找有没有缓存的DNS记录，如果在浏览器缓存没有找到需要的记录，就会去做一个系统的调用，获取系统缓存的记录；
`

`
如果没有记录请求会继续到路由器上，路由器上有自己的DNS缓存；
`

`
如果没有记录就会到ISP的DNS缓存中查看记录；
`

`
如果没有记录就会在ISP的DNS服务器从根服务器域名服务器开始递归搜索最后得到IP地址;
`

`
浏览器给baidu服务器发送一个HTTP请求
`