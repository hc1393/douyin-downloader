// pages/login/login.js
Page({
  data: {
    username: '',
    password: ''
  },

  /**
   * 监听用户名输入
   */
  onUsernameInput: function(e) {
    this.setData({
      username: e.detail.value
    });
  },

  /**
   * 监听密码输入
   */
  onPasswordInput: function(e) {
    this.setData({
      password: e.detail.value
    });
  },

  /**
   * 登录按钮点击事件
   */
  onLogin: function(e) {
    const { username, password } = e.detail.value;
    
    // 表单验证
    if (!username) {
      wx.showToast({
        title: '请输入用户名',
        icon: 'none'
      });
      return;
    }
    
    if (!password) {
      wx.showToast({
        title: '请输入密码',
        icon: 'none'
      });
      return;
    }
    
    // 显示加载提示
    wx.showLoading({
      title: '登录中...'
    });
    
    // 模拟登录请求（实际开发中需要替换为真实的API调用）
    setTimeout(() => {
      wx.hideLoading();
      
      // 模拟登录成功
      if (username === 'admin' && password === '123456') {
        wx.showToast({
          title: '登录成功',
          icon: 'success'
        });
        
        // 存储用户信息
        wx.setStorageSync('isLogin', true);
        wx.setStorageSync('username', username);
        
        // 跳转到首页
        wx.switchTab({
          url: '../home/home'
        });
      } else {
        wx.showToast({
          title: '用户名或密码错误',
          icon: 'none'
        });
      }
    }, 1500);
  },

  /**
   * 微信登录
   */
  wechatLogin: function() {
    wx.showToast({
      title: '微信登录',
      icon: 'none'
    });
  },

  /**
   * QQ登录
   */
  qqLogin: function() {
    wx.showToast({
      title: 'QQ登录',
      icon: 'none'
    });
  },

  /**
   * 微博登录
   */
  weiboLogin: function() {
    wx.showToast({
      title: '微博登录',
      icon: 'none'
    });
  }
});