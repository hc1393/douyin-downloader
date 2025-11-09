// pages/home/home.js
Page({
  data: {},

  onLoad: function (options) {
    // 页面加载时检查登录状态
    const isLogin = wx.getStorageSync('isLogin');
    if (!isLogin) {
      wx.redirectTo({
        url: '../login/login'
      });
    }
  },

  onLogout: function() {
    // 清除登录状态
    wx.removeStorageSync('isLogin');
    wx.removeStorageSync('username');
    
    // 跳转到登录页
    wx.redirectTo({
      url: '../login/login'
    });
  }
});