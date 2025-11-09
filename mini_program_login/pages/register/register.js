// pages/register/register.js
Page({
  data: {

  },

  /**
   * 注册表单提交
   */
  onRegister: function(e) {
    const { username, mobile, password, confirmPassword } = e.detail.value;
    
    // 表单验证
    if (!username) {
      wx.showToast({
        title: '请输入用户名',
        icon: 'none'
      });
      return;
    }
    
    if (!mobile) {
      wx.showToast({
        title: '请输入手机号',
        icon: 'none'
      });
      return;
    }
    
    // 简单手机号验证
    if (!/^1[3-9]\d{9}$/.test(mobile)) {
      wx.showToast({
        title: '手机号格式不正确',
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
    
    if (password !== confirmPassword) {
      wx.showToast({
        title: '两次输入的密码不一致',
        icon: 'none'
      });
      return;
    }
    
    // 显示加载提示
    wx.showLoading({
      title: '注册中...'
    });
    
    // 模拟注册请求（实际开发中需要替换为真实的API调用）
    setTimeout(() => {
      wx.hideLoading();
      
      // 模拟注册成功
      wx.showToast({
        title: '注册成功',
        icon: 'success'
      });
      
      // 延迟跳转到登录页
      setTimeout(() => {
        wx.redirectTo({
          url: '../login/login'
        });
      }, 1500);
    }, 1500);
  }
});