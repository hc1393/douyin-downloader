// pages/forgot/forgot.js
Page({
  data: {
    countdown: 0,
    timer: null
  },

  /**
   * 获取验证码
   */
  getCode: function() {
    // 检查是否正在倒计时
    if (this.data.countdown > 0) {
      return;
    }
    
    // 这里应该调用获取验证码的接口
    wx.showToast({
      title: '验证码已发送',
      icon: 'none'
    });
    
    // 设置60秒倒计时
    this.setData({
      countdown: 60
    });
    
    this.data.timer = setInterval(() => {
      let count = this.data.countdown - 1;
      this.setData({
        countdown: count
      });
      
      if (count <= 0) {
        clearInterval(this.data.timer);
      }
    }, 1000);
  },

  /**
   * 重置密码
   */
  onResetPassword: function(e) {
    const { mobile, code, newPassword } = e.detail.value;
    
    // 表单验证
    if (!mobile) {
      wx.showToast({
        title: '请输入手机号',
        icon: 'none'
      });
      return;
    }
    
    if (!code) {
      wx.showToast({
        title: '请输入验证码',
        icon: 'none'
      });
      return;
    }
    
    if (!newPassword) {
      wx.showToast({
        title: '请输入新密码',
        icon: 'none'
      });
      return;
    }
    
    // 显示加载提示
    wx.showLoading({
      title: '重置中...'
    });
    
    // 模拟重置密码请求（实际开发中需要替换为真实的API调用）
    setTimeout(() => {
      wx.hideLoading();
      
      // 模拟重置成功
      wx.showToast({
        title: '密码重置成功',
        icon: 'success'
      });
      
      // 延迟跳转到登录页
      setTimeout(() => {
        wx.navigateBack();
      }, 1500);
    }, 1500);
  },

  /**
   * 页面卸载时清除定时器
   */
  onUnload: function() {
    if (this.data.timer) {
      clearInterval(this.data.timer);
    }
  }
});