const axios = require('axios'); // Node.js 环境
// 浏览器环境直接使用 axios（需提前引入）

const url='https://www.acgice.com/sjz/v/keys?t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTI5NjEsIm5hbWUiOiI1MDkwMzFBMzZDQUExRkY1MUU1QUUzNzdGODg4QTA5OCIsImdyb3VwX2lkIjoxLCJwYXJlbnRfaWQiOjAsInR5cGUiOiIiLCJjcmVhdGVfdGltZSI6IjIwMjUtMDktMTRUMTM6MTM6MjguNTIyNjAxNjE5KzA4OjAwIiwiZXhwIjoxNzU3ODYyODA4fQ.nyECeZydboLUccDj1QuIU7um6Zxb-DIwht1JGvuw3so'   ; // 使用完整URL

axios.get(url)
  .then(response => {
    // 匹配 HTML 中的 TimeUnix 定义
    const regex = /var TimeUnix = (\d+);/;
    const match = response.data.match(regex);

    if (match) {
      const timeUnix = parseInt(match[1]);
      console.log("提取到的 TimeUnix:", timeUnix);
    } else {
      console.error("未找到 TimeUnix 值");
    }
  })
  .catch(error => {
    console.error("请求失败:", error.message);
  })

   var TimeUnixBD = Math.round(new Date().getTime() / 1000);
            var TimeUnixDiff = TimeUnixBD - TimeUnix;
            function GetTimeUnix() {
                let time_unix = Math.round(new Date().getTime() / 1000);
                return time_unix - TimeUnixDiff;
            }