// pages/login/login.js
Page({
  data: {
    username: '',
    password: '',
    showPassword: false,
    rememberPassword: false,
    autoLogin: false
  },

  onLoad: function() {
    // 页面加载时检查是否记住密码
    const rememberInfo = wx.getStorageSync('rememberInfo');
    if (rememberInfo) {
      this.setData({
        username: rememberInfo.username || '',
        password: rememberInfo.password || '',
        rememberPassword: true
      });
    }
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
   * 切换密码可见性
   */
  togglePasswordVisibility: function() {
    this.setData({
      showPassword: !this.data.showPassword
    });
  },

  /**
   * 记住密码选项更改
   */
  onRememberPasswordChange: function(e) {
    this.setData({
      rememberPassword: e.detail.value
    });
  },

  /**
   * 自动登录选项更改
   */
  onAutoLoginChange: function(e) {
    this.setData({
      autoLogin: e.detail.value
    });
  },

  /**
   * 登录按钮点击事件
   */
  onLogin: function(e) {
    const { username, password } = this.data;
    
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
    
    // 根据选项决定是否记住密码
    if (this.data.rememberPassword) {
      wx.setStorageSync('rememberInfo', {
        username: this.data.username,
        password: this.data.password
      });
    } else {
      wx.removeStorageSync('rememberInfo');
    }
    
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