let globalSessionToken = null;

function generateSessionToken() {
  const _0x2c4403 = {
    "randomString": Math.random().toString(36).substring(2)
  };
  return btoa(JSON.stringify(_0x2c4403));
}

function setSessionToken() {
  !globalSessionToken && (globalSessionToken = generateSessionToken(), localStorage.setItem("session_token", globalSessionToken));
}

function getSessionToken() {
  return globalSessionToken || localStorage.getItem("session_token");
}

setSessionToken();
document.querySelector(".video-input button").addEventListener("mousedown", function () {
  var _0x3546bd = document.querySelector(".video-input input");

  !_0x3546bd.matches(":focus") && (_0x3546bd.style.borderColor = "#007bff");
});
document.querySelector(".video-input button").addEventListener("mouseup", function () {
  var _0xa82e73 = document.querySelector(".video-input input");

  !_0xa82e73.matches(":focus") && (_0xa82e73.style.borderColor = "#ccc");
});
document.querySelector(".video-input input").addEventListener("focus", function () {
  this.style.borderColor = "#007bff";
});
document.querySelector(".video-input input").addEventListener("blur", function () {
  this.style.borderColor = "#ccc";
});

function logout() {
  document.getElementById("userDisplay").innerText = "";
  document.getElementById("logoutButton").style.display = "none";
  document.getElementById("loginButton").style.display = "inline-block";
  document.getElementById("registerButton").style.display = "inline-block";
}

async function setValue() {
  const _0x5a3415 = document.getElementById("url").value.trim();

  const _0x20a2a1 = document.querySelector(".down");

  const _0x1bff2a = document.getElementById("loadingSpinner");

  if (!_0x5a3415) {
    _0x20a2a1.innerHTML = "<p>输入不能为空<br/></p>";
    return;
  }

  const _0x5e1cc7 = /http[s]?:\/\/[\w.-]+[\w\/-]*[\w.-]*\??[\w=&:\-\+\%]*[/]*/;
  const _0x1c710f = /https?:\/\/(?:www|m|vt|vm)?\.tiktok\.com\/(?:@[\w.-]+\/video\/\d+|[\w.-]+)|https?:\/\/(?:www\.)?douyin\.com\/(?:v|video)\/[\w.-]+|https?:\/\/v\.douyin\.com\/[\w.-]+/g;

  const _0x431bf1 = _0x11b21b => _0x11b21b.includes("tiktok.com");

  let _0x484210;

  try {
    if (_0x431bf1(_0x5a3415)) {
      _0x484210 = _0x5a3415.match(_0x1c710f)?.[0];
    } else {
      _0x484210 = _0x5a3415.match(_0x5e1cc7)?.[0];
    }

    if (!_0x484210) throw new Error("未检测到有效链接");
  } catch (_0x5249f2) {
    console.log(_0x5249f2);

    const _0x2ab667 = "\n            <p>解析失败: " + _0x5249f2.message + "<br/></p>\n            <h4 style=\"margin: 20px auto; font-size: 15px;\">欢迎加入我们的群聊一起交流、反馈，我们会随时提供帮助！</h4>\n            <img src=\"/static/img/jiaoliuqun.jpg\" class=\"wechat-image\" alt=\"微信群二维码\" style=\"display: block; margin: 20px auto; max-width: 200px; border: 1px solid #ddd; border-radius: 8px;\" />\n        ";

    _0x20a2a1.innerHTML = _0x2ab667;
    return;
  }

  const _0x6440d8 = getSessionToken();

  _0x1bff2a.style.display = "flex";

  try {
    const _0x595b17 = await fetch("/api/video/share/url/parse", {
      "method": "POST",
      "headers": {
        "Content-Type": "application/json",
        "Origin": window.location.origin,
        "X-Requested-By": "web",
        "Session-Token": _0x6440d8
      },
      "body": JSON.stringify({
        "url": _0x484210,
        "key": "dd87bbb8-6306-467e-8711-ff771a281020"
      })
    });

    if (!_0x595b17.ok) {
      if (_0x595b17.status === 500) {
        const _0x5a36de = await _0x595b17.text();

        const _0x3305b6 = "\n                    <p>访问过于频繁，请稍后再试！</p>\n                    <h4 style=\"margin: 20px auto; font-size: 15px;\">欢迎加入我们的群聊一起交流、反馈，我们会随时提供帮助！</h4>\n                    <img src=\"/static/img/jiaoliuqun.jpg\" class=\"wechat-image\" alt=\"微信群二维码\" style=\"display: block; margin: 20px auto; max-width: 200px; border: 1px solid #ddd; border-radius: 8px;\" />\n                ";
        _0x20a2a1.innerHTML = _0x3305b6;
        return;
      }
    }

    const _0x31e4ed = await _0x595b17.json();

    if (_0x31e4ed.code === 200) {
      mdui.snackbar({
        "message": "解析成功"
      });

      let _0x191689 = "<h4>" + _0x31e4ed.data.title + "</h4>";

      _0x31e4ed.data.video_url && (_0x191689 += "\n                <div class=\"video-container\">\n                    <video controls=\"controls\" autoplay muted width=\"100%\" height=\"100%\" volume=\"0.5\" style=\"max-height: 400px; margin: 1em 0;\">\n                        <source src=\"" + _0x31e4ed.data.video_url + "\" type=\"video/mp4\">\n                    </video>\n                </div><br>\n            ", _0x191689 += "<a class=\"btn\" href=\"" + _0x31e4ed.data.video_url + "\" target=\"_blank\" download=\"video.mp4\" rel=\"noreferrer\">下载视频</a>");
      _0x31e4ed.data.cover_url && (_0x191689 += "<a class=\"btn\" href=\"" + _0x31e4ed.data.cover_url + "\" target=\"_blank\" download=\"cover.jpg\" rel=\"noreferrer\">下载封面</a>");
      _0x31e4ed.data.images?.["length"] > 0 && (_0x191689 += "<h4>图集</h4>", _0x31e4ed.data.images.forEach(_0x32db08 => {
        _0x191689 += "<img src=\"" + _0x32db08 + "\" style=\"width: 160px; margin: 1em;\" />";
      }));
      const _0x1e26fb = "\n            <h4 style=\"margin: 20px auto; font-size: 20px;\">\n                <font color=\"#FF0000\">如果下载失败，请尝试在下载按钮上点击鼠标右键，然后选择\"链接另存为\"</font>\n            </h4>\n            <h4 style=\"margin: 20px auto; font-size: 15px;\">\n                欢迎加入我们的群聊一起交流、反馈，我们会随时提供帮助！\n            </h4>\n            <img src=\"/static/img/jiaoliuqun.jpg\" class=\"wechat-image\" alt=\"微信群二维码\" style=\"display: block; margin: 20px auto; max-width: 200px; border: 1px solid #ddd; border-radius: 8px;\" />\n        ";
      _0x191689 += _0x1e26fb;
      _0x20a2a1.innerHTML = _0x191689;
    } else {
      const _0x374cf0 = "\n            <p>解析失败,视频不存在或者链接不正确:<br/></p>\n            <h4 style=\"margin: 20px auto; font-size: 15px;\">欢迎加入我们的群聊一起交流、反馈，我们会随时提供帮助！</h4>\n            <img src=\"/static/img/jiaoliuqun.jpg\" class=\"wechat-image\" alt=\"微信群二维码\" style=\"display: block; margin: 20px auto; max-width: 200px; border: 1px solid #ddd; border-radius: 8px;\" />\n        ";
      _0x20a2a1.innerHTML = _0x374cf0;
      mdui.snackbar({
        "message": "解析失败: " + _0x31e4ed.msg
      });
    }
  } catch (_0x10f450) {
    console.log(_0x10f450);

    const _0x18cb7c = "\n            <p>解析失败: " + _0x10f450.message + "<br/></p>\n            <h4 style=\"margin: 20px auto; font-size: 15px;\">欢迎加入我们的群聊一起交流、反馈，我们会随时提供帮助！</h4>\n            <img src=\"/static/img/jiaoliuqun.jpg\" class=\"wechat-image\" alt=\"微信群二维码\" style=\"display: block; margin: 20px auto; max-width: 200px; border: 1px solid #ddd; border-radius: 8px;\" />\n        ";

    _0x20a2a1.innerHTML = _0x18cb7c;
    console.error(_0x10f450);
  } finally {
    _0x1bff2a.style.display = "none";
  }
}