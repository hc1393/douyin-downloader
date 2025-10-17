var __defProp = Object.defineProperty,
  __defProps = Object.defineProperties,
  __getOwnPropDescs = Object.getOwnPropertyDescriptors,
  __getOwnPropSymbols = Object.getOwnPropertySymbols,
  __hasOwnProp = Object.prototype.hasOwnProperty,
  __propIsEnum = Object.prototype.propertyIsEnumerable,
  __defNormalProp = (e, t, i) => t in e ? __defProp(e, t, {
    enumerable: !0,
    configurable: !0,
    writable: !0,
    value: i
  }) : e[t] = i,
  __spreadValues = (e, t) => {
    for (var i in t || (t = {})) __hasOwnProp.call(t, i) && __defNormalProp(e, i, t[i]);
    if (__getOwnPropSymbols)
      for (var i of __getOwnPropSymbols(t)) __propIsEnum.call(t, i) && __defNormalProp(e, i, t[i]);
    return e
  },
  __spreadProps = (e, t) => __defProps(e, __getOwnPropDescs(t)),
  __async = (e, t, i) => new Promise((n, o) => {
    var r = e => {
        try {
          a(i.next(e))
        } catch (e) {
          o(e)
        }
      },
      s = e => {
        try {
          a(i.throw(e))
        } catch (e) {
          o(e)
        }
      },
      a = e => e.done ? n(e.value) : Promise.resolve(e.value).then(r, s);
    a((i = i.apply(e, t)).next())
  }),
  g = {};
g.c = require("./bundle.js"), (g.c = g.c || []).push([
  [15], {
    0: function (e, t, i) {
      i(192), i.g.currentModuleId = "mpx-app-scope", i.g.currentCtor = App, i.g.currentCtorType = "app", i.g.currentResourceType = "app", i.g.qmaiPageTitles = {
        pages: [{
          path: "pages/index/index",
          title: "首页"
        }, {
          path: "pages/user/index",
          title: "个人中心"
        }, {
          path: "pages/takefood/index",
          title: "点单页"
        }, {
          path: "pages/takeout/index",
          title: "外卖点单页"
        }, {
          path: "pages/page/page",
          title: "自定义页面"
        }, {
          path: "pages/order/list/index",
          title: "订单列表"
        }, {
          path: "pages/pay/index/index",
          title: "买单"
        }, {
          path: "subpackages/payment-code/index",
          title: "会员码"
        }, {
          path: "pages/duibaPay/duibaPay",
          title: "兑吧"
        }, {
          path: "pages/duibaRedirect/duibaRedirect",
          title: "兑吧"
        }, {
          path: "pages/page/p1/index",
          title: "自定义页面1"
        }, {
          path: "pages/page/p2/index",
          title: "自定义页面2"
        }, {
          path: "pages/page/p3/index",
          title: "自定义页面3"
        }, {
          path: "pages/page/p4/index",
          title: "自定义页面4"
        }, {
          path: "pages/page/p5/index",
          title: "自定义页面5"
        }, {
          path: "pages/pluginMall/index",
          title: "商城"
        }, {
          path: "pages/webView/index",
          title: "webView"
        }, {
          path: "subpackages/license/index",
          title: "食品安全档案"
        }, {
          path: "pages/user/qualification/index",
          title: "服务资质"
        }, {
          path: "pages/pay/record/index",
          title: "买单记录"
        }, {
          path: "subpackages/webView/index",
          title: "webView"
        }, {
          path: "subpackages/privacyNumPage/index",
          title: "号码保护"
        }, {
          path: "pages/order/remark/index",
          title: "订单备注"
        }, {
          path: "subpackages/errorPage/index",
          title: "小程序异常页面"
        }, {
          path: "subpackages/pay-gift-other-rights/index",
          title: "QQ权益"
        }, {
          path: "pages/pay/detail/index",
          title: "买单订单详情"
        }, {
          path: "subpackages/delivery-detail/index",
          title: "订单详情"
        }, {
          path: "pluginMall/error/index",
          title: "系统错误"
        }, {
          path: "pluginMall/webview/index",
          title: "webview"
        }, {
          path: "pluginMall/index/index",
          title: "商城-首页"
        }, {
          path: "pluginMall/classify/index",
          title: "商品分类"
        }, {
          path: "pluginMall/detail/index",
          title: "商品详情页"
        }, {
          path: "pluginMall/cart/index",
          title: "购物车"
        }, {
          path: "pluginMall/order-confirm/index",
          title: "提交订单"
        }, {
          path: "pluginMall/order-detail/index",
          title: "订单详情"
        }, {
          path: "pluginMall/order-list/index",
          title: "订单列表"
        }, {
          path: "pluginMall/logistics-detail/index",
          title: "物流信息"
        }, {
          path: "pluginMall/logistics-form/index",
          title: "物流信息"
        }, {
          path: "pluginMall/after-sale-select/index",
          title: "选择售后类型"
        }, {
          path: "pluginMall/after-sale-form/index",
          title: "退款申请"
        }, {
          path: "pluginMall/after-sale-detail/index",
          title: "售后详情"
        }, {
          path: "pluginMall/address-list/index",
          title: "地址列表"
        }, {
          path: "pluginMall/address-edit/index",
          title: "地址编辑"
        }, {
          path: "pluginMall/invoicing-detail/index",
          title: "开票详情"
        }, {
          path: "pluginMall/distribution-index/index",
          title: "分销中心"
        }, {
          path: "pluginMall/distribution-apply/index",
          title: "申请成为分销员"
        }, {
          path: "pluginMall/distribution-invite/index",
          title: "邀请分销员"
        }, {
          path: "pluginMall/distribution-junior/index",
          title: "下级分销员"
        }, {
          path: "pluginMall/distribution-withdraw/index",
          title: "分销 提现"
        }, {
          path: "pluginMall/distribution-withdraw-record/index",
          title: "分销提现记录"
        }, {
          path: "pluginMall/distribution-order/index",
          title: "分销订单"
        }, {
          path: "pluginMall/distribution-goods/index",
          title: "分销商品列表"
        }, {
          path: "pluginMall/pay-result/index",
          title: "支付结果"
        }, {
          path: "pluginMall/order-change/index",
          title: "修改订单"
        }, {
          path: "pluginMall/store-select/index",
          title: "门店列表"
        }, {
          path: "pluginMall/city-select/index",
          title: "选择门店"
        }, {
          path: "pluginMall/goods-search/index",
          title: "商品搜索"
        }, {
          path: "pluginPoint/index/index",
          title: "积分商城-首页"
        }, {
          path: "pluginPoint/record/index",
          title: "明细"
        }, {
          path: "pluginPoint/rule/index",
          title: "规则"
        }, {
          path: "pluginPoint/exchange-record/index",
          title: "兑换记录"
        }, {
          path: "pluginPoint/exchange-coupon/index",
          title: "兑换商品"
        }, {
          path: "pluginPoint/exchange-evaluate/index",
          title: "评价"
        }, {
          path: "pluginPoint/exchange-success/index",
          title: "兑换信息"
        }, {
          path: "pluginPoint/exchange-order-confirm/index",
          title: "确认兑换"
        }, {
          path: "pluginPoint/exchange-confirm/index",
          title: "确认兑换"
        }, {
          path: "pluginPoint/entity-exchange-success/index",
          title: "兑换成功"
        }, {
          path: "pluginPoint/logistics/index",
          title: "兑换物流"
        }, {
          path: "pluginPoint/refund-apply/index",
          title: "退款"
        }, {
          path: "pluginPoint/refund-list/index",
          title: "退款明细"
        }, {
          path: "pluginPoint/refund-detail/index",
          title: "退款详情"
        }, {
          path: "pluginPoint/pay-result/index",
          title: "支付成功"
        }, {
          path: "pluginPoint/webview/index",
          title: ""
        }, {
          path: "pluginPages/login-guide/index",
          title: ""
        }, {
          path: "pluginPages/money-saving-calc/index",
          title: "xxx"
        }, {
          path: "pluginPages/store-account/index",
          title: "账户详情"
        }, {
          path: "pluginPages/transaction-records/index",
          title: "交易记录"
        }, {
          path: "pluginPages/applicable-stores/index",
          title: "所属门店"
        }, {
          path: "pluginPages/mall-invoice-apply/index",
          title: "申请发票"
        }, {
          path: "pluginPages/mall-invoice-detail/index",
          title: "发票详情"
        }, {
          path: "pluginPages/goods-energy-calculation/index",
          title: "能量详情"
        }, {
          path: "pluginPages/apply-stores/index",
          title: "适用门店"
        }, {
          path: "pluginPages/apply-goods/index",
          title: "适用商品"
        }, {
          path: "pluginPages/apply-rights-cards/index",
          title: "适用权益卡"
        }, {
          path: "pluginPages/apply-gift-cards/index",
          title: "适用礼品卡"
        }, {
          path: "pluginPages/custom-web-view/index",
          title: "自定义webview"
        }, {
          path: "pluginPages/miniapp-bridge/index",
          title: "桥页面"
        }, {
          path: "pluginPages/privacy-policy/index",
          title: "隐私协议页面"
        }, {
          path: "pluginPages/rich-text/index",
          title: "富文本"
        }, {
          path: "pluginPages/student-certification/index",
          title: "学生认证"
        }, {
          path: "pluginDine/address-add/index",
          title: "新增地址"
        }, {
          path: "pluginDine/address-edit/index",
          title: "编辑地址"
        }, {
          path: "pluginDine/address-select/index",
          title: "选择地址"
        }, {
          path: "pluginDine/location-select/index",
          title: "选择地点"
        }, {
          path: "pluginDine/goods-package-detail/index",
          title: "套餐商品详情"
        }, {
          path: "pluginDine/goods-list/index",
          title: "商品列表"
        }, {
          path: "pluginDine/goods-search/index",
          title: "商品搜索"
        }, {
          path: "pluginDine/goods-packing-fee-detail/index",
          title: "包装费说明"
        }, {
          path: "pluginDine/order-confirm/index",
          title: "确认订单"
        }, {
          path: "pluginDine/order-detail/index",
          title: "订单详情"
        }, {
          path: "pluginDine/order-list/index",
          title: "订单列表"
        }, {
          path: "pluginDine/order-remark/index",
          title: "订单备注"
        }, {
          path: "pluginDine/refund-apply/index",
          title: "申请退款"
        }, {
          path: "pluginDine/refund-detail/index",
          title: "退款详情"
        }, {
          path: "pluginDine/refund-list/index",
          title: "退款记录"
        }, {
          path: "pluginDine/shop-select/index",
          title: "选择门店"
        }, {
          path: "pluginDine/shop-cert/service-qualification",
          title: "服务资质"
        }, {
          path: "pluginDine/shop-cert/food-safety-file",
          title: "食品安全档案"
        }, {
          path: "pluginDine/shop-activity/detail",
          title: "活动详情"
        }, {
          path: "pluginDine/invoice-detail/index",
          title: "开票详情"
        }, {
          path: "pluginDine/invoice-select/index",
          title: "发票抬头"
        }, {
          path: "pluginDine/invoice-add/index",
          title: "新增发票抬头"
        }, {
          path: "pluginDine/invoice-apply/index",
          title: "申请开票"
        }, {
          path: "pluginMedal/index/index",
          title: "勋章"
        }, {
          path: "pluginMedal/medal-detail/index",
          title: "勋章详情"
        }, {
          path: "pluginMedal/task/index",
          title: "勋章任务"
        }, {
          path: "pluginMedal/task-rewards/index",
          title: "我的奖励"
        }, {
          path: "pluginUser/index",
          title: "我的"
        }, {
          path: "pluginUser/account-mgmt/index",
          title: "账号管理"
        }, {
          path: "pluginUser/account-switch/index",
          title: "切换账号"
        }, {
          path: "pluginUser/account-log-off/index",
          title: "账号注销"
        }, {
          path: "pluginUser/log-off-agreement/index",
          title: "注销协议"
        }, {
          path: "pluginUser/assets-move/index",
          title: "资产迁移"
        }, {
          path: "pluginUser/assets-move-records/index",
          title: "资产迁移记录"
        }, {
          path: "pluginQueue/index",
          title: "排队"
        }, {
          path: "pluginFeedback/index/index",
          title: "建议反馈"
        }, {
          path: "pluginFeedback/add/index",
          title: "建议反馈"
        }, {
          path: "subpackages/tabbar-pages/takefood/index",
          title: "点单页"
        }, {
          path: "subpackages/tabbar-pages/order-list/index",
          title: "订单列表页"
        }, {
          path: "subpackages/tabbar-pages/pay/index",
          title: "买单页"
        }, {
          path: "async-components/index",
          title: "异步组件分包"
        }, {
          path: "async-components2/index",
          title: "异步组件分包2"
        }, {
          path: "open/index",
          title: "开放能力分包"
        }, {
          path: "subpackages/tabbar-pages/user/index",
          title: "个人中心"
        }, {
          path: "subpackages/tabbar-pages/index/index",
          title: "首页"
        }, {
          path: "subpackages/tabbar-pages/page/index",
          title: "装修页面"
        }, {
          path: "pluginMarketing/lottery/index/index",
          title: "抽奖"
        }, {
          path: "pluginMarketing/lottery/share/index",
          title: "分享"
        }, {
          path: "pluginMarketing/lottery/join/index",
          title: "参与记录"
        }, {
          path: "pluginMarketing/lottery/rule/index",
          title: "活动规则"
        }, {
          path: "pluginMarketing/lottery/equity/index",
          title: "三方权益"
        }, {
          path: "pluginMarketing/checkin/index/index",
          title: "签到有礼"
        }, {
          path: "pluginMarketing/checkin/my-reward/index",
          title: "我的奖品"
        }, {
          path: "pluginMarketing/receive/index/index",
          title: "领取活动"
        }, {
          path: "pluginMarketing/receive/list/index",
          title: "领取活动 列表"
        }, {
          path: "pluginMarketing/receive/receive-result/index",
          title: "领取结果"
        }, {
          path: "pluginMarketing/receive/password-rule/index",
          title: "如何获取口令"
        }, {
          path: "pluginMarketing/partition-coupon/index/index",
          title: "瓜分优惠券"
        }, {
          path: "pluginMarketing/partition-coupon/team-record/index",
          title: "瓜分优惠券我的记录"
        }, {
          path: "pluginMarketing/point-exchange/index/index",
          title: "积分换礼"
        }, {
          path: "pluginMarketing/point-exchange/detail/index",
          title: "积分换礼详情"
        }, {
          path: "pluginMarketing/point-exchange/my-reward/index",
          title: "积分换礼我的奖品"
        }, {
          path: "pluginMarketing/point-exchange/goods/index",
          title: "积分换礼适用商品"
        }, {
          path: "pluginMarketing/point-exchange/store/index",
          title: "积分换礼适用门店"
        }, {
          path: "pluginMarketing/bridge/subscribe/index",
          title: "中转页 订阅消息"
        }, {
          path: "pluginMarketing/bridge/navigate/index",
          title: "中转页 跳转"
        }, {
          path: "pluginMarketing/bridge/crowd/index",
          title: "中转页 人群弹窗"
        }, {
          path: "pluginMarketing/bridge/authorization/index",
          title: "中转页 用户授权"
        }, {
          path: "pluginMarketing/common/web-view/index",
          title: "公用页面 webview"
        }, {
          path: "pluginMarketing/common/my-reward/index",
          title: "公用页面我的奖品"
        }, {
          path: "pluginMarketing/common/reward-template-detail",
          title: "奖品模板详情"
        }, {
          path: "pluginMarketing/common/my-reward/coupon-package-detail",
          title: "我的奖品之券包详情"
        }, {
          path: "pluginMarketing/common/goods/index",
          title: "公用页面适用商品"
        }, {
          path: "pluginMarketing/common/goods/common-goods",
          title: "通用适用商品"
        }, {
          path: "pluginMarketing/common/store/index",
          title: "公用页面适用门店"
        }, {
          path: "pluginMarketing/common/source/index",
          title: "订单来源渠道"
        }, {
          path: "pluginMarketing/collect-card/index/index",
          title: "集卡活动"
        }, {
          path: "pluginMarketing/collect-card/get-card/index",
          title: "集卡活动 领卡页"
        }, {
          path: "pluginMarketing/collect-card/my-card/index",
          title: "我的卡片"
        }, {
          path: "pluginMarketing/collect-card/give-record/index",
          title: "集卡活动 赠送记录"
        }, {
          path: "pluginMarketing/nurture/index/index",
          title: "养成活动首页"
        }, {
          path: "pluginMarketing/invite/index/index",
          title: "邀请活动首页"
        }, {
          path: "pluginMarketing/invite/share/index",
          title: "邀请活动 分享页"
        }, {
          path: "pluginMarketing/invite/my-invite/index",
          title: "邀请活动 我的邀请记录"
        }, {
          path: "pluginMarketing/guess/index/index",
          title: "竞猜活动"
        }, {
          path: "pluginMarketing/guess/record/index",
          title: "竞猜记录"
        }, {
          path: "pluginMarketing/guess/reward/index",
          title: "我的奖品"
        }, {
          path: "pluginMarketing/exchange/index/index",
          title: "兑换有礼"
        }, {
          path: "pluginMarketing/activity-center/index/index",
          title: "活动中心"
        }, {
          path: "pluginMarketing/activity-center/detail/index",
          title: "活动中心"
        }, {
          path: "pluginMarketing/overlord-meal/index",
          title: "霸王餐"
        }, {
          path: "pluginMarketing/overlord-meal/share",
          title: "分享"
        }, {
          path: "pluginMarketing/identify-customer-code/index",
          title: "识客码"
        }, {
          path: "pluginMarketing/collect-img/index/index",
          title: "集卡活动"
        }, {
          path: "pluginMarketing/collect-img/give-record/index",
          title: "集卡活动 赠送记录"
        }, {
          path: "pluginMarketing/scratchcard/index/index",
          title: "刮刮卡"
        }, {
          path: "pluginMarketing/scratchcard/share/index",
          title: "刮刮卡 分享"
        }, {
          path: "pluginMarketing/decibel/index",
          title: "最强分贝"
        }, {
          path: "pluginMarketing/puzzle/index",
          title: "拼图游戏"
        }, {
          path: "pluginMarketing/puzzle/give-record",
          title: "拼图游戏-赠送记录"
        }, {
          path: "pluginMarketing/puzzle/get-pieces",
          title: "拼图游戏-领碎片"
        }, {
          path: "pluginMarketing/ladder-coupons/index",
          title: "按序核券"
        }, {
          path: "pluginMarketing/funny-synthesis/index/index",
          title: "趣味合成"
        }, {
          path: "pluginMarketing/funny-synthesis/give-record/index",
          title: "趣味合成 赠送记录"
        }, {
          path: "pluginMedal/index/index",
          title: "勋章"
        }, {
          path: "pluginMedal/medal-detail/index",
          title: "勋章详情"
        }, {
          path: "pluginMedal/task/index",
          title: "勋章任务"
        }, {
          path: "pluginMedal/task-rewards/index",
          title: "我的奖励"
        }, {
          path: "subpackages/bargain/list/index",
          title: "砍价列表"
        }, {
          path: "subpackages/bargain/equity-card/index",
          title: "砍价详情"
        }, {
          path: "subpackages/bargain/equity-order/index",
          title: "砍价确认订单"
        }, {
          path: "subpackages/bargain/activity/index",
          title: "砍价详情"
        }, {
          path: "subpackages/bargain/record/index",
          title: "砍价记录"
        }, {
          path: "subpackages/old-bring-new/index/index",
          title: "老带新"
        }, {
          path: "subpackages/old-bring-new/help/index",
          title: "老带新助力"
        }, {
          path: "subpackages/old-bring-new/rule/index",
          title: "老带新活动规则"
        }, {
          path: "subpackages/old-bring-new/reward/index",
          title: "老带新奖励"
        }, {
          path: "subpackages/old-bring-new/share/index",
          title: "老带新分享"
        }, {
          path: "subpackages/invite-for-gift/index/index",
          title: "邀请有礼"
        }, {
          path: "subpackages/invite-for-gift/help/index",
          title: "邀请有礼助力"
        }, {
          path: "subpackages/invite-for-gift/rule/index",
          title: "邀请有礼活动规则"
        }, {
          path: "subpackages/invite-for-gift/reward/index",
          title: "邀请有礼我的奖励"
        }, {
          path: "subpackages/invite-for-gift/share/index",
          title: "邀请有礼海报页面"
        }, {
          path: "subpackages/integralDraw/index/index",
          title: "积分抽奖"
        }, {
          path: "subpackages/integralDraw/rule/index",
          title: "积分抽奖活动规则"
        }, {
          path: "subpackages/treasure/index/index",
          title: "集星有礼"
        }, {
          path: "subpackages/treasure/my-treasure/index",
          title: "我的集星"
        }, {
          path: "subpackages/treasure/coupon-list/index",
          title: "集星有礼领券列表"
        }, {
          path: "subpackages/treasure/get-coupon/index",
          title: "集星有礼领券"
        }, {
          path: "subpackages/treasure/actList/index",
          title: "集星有礼"
        }, {
          path: "subpackages/spellGroup/list/index",
          title: "拼团列表"
        }, {
          path: "subpackages/spellGroup/detail/index",
          title: "拼团活动详情"
        }, {
          path: "subpackages/spellGroup/groupTeamDetail/index",
          title: "拼团详情"
        }, {
          path: "subpackages/questionAnswer/index",
          title: "问卷调查"
        }, {
          path: "subpackages/questionAnswerNew/index",
          title: "新问卷调查"
        }, {
          path: "subpackages/blindBoxLottery/index",
          title: "盲盒抽奖"
        }, {
          path: "subpackages/spell-coupon/list/index",
          title: "拼券列表"
        }, {
          path: "subpackages/spell-coupon/order/confirm/index",
          title: "拼券确认订单"
        }, {
          path: "subpackages/spell-coupon/order/success/index",
          title: "拼券成功"
        }, {
          path: "subpackages/spell-coupon/order/list/index",
          title: "拼券订单列表"
        }, {
          path: "subpackages/spell-coupon/order/detail/index",
          title: "拼券订单详情"
        }, {
          path: "subpackages/spell-coupon/applicable/index",
          title: "拼券适用商品"
        }, {
          path: "subpackages/spell-coupon/detail/index",
          title: "拼券活动详情"
        }, {
          path: "subpackages/spell-coupon/group-detail/index",
          title: "拼券团详情"
        }, {
          path: "subpackages/spell-coupon/group-list/index",
          title: "拼券团列表"
        }, {
          path: "subpackages/spell-coupon/members/index",
          title: "拼券团成员"
        }, {
          path: "subpackages/password-envelope/index/index",
          title: "口令红包"
        }, {
          path: "subpackages/password-envelope/reward/index",
          title: "口令红包-我的奖励"
        }, {
          path: "subpackages/outbreak-card/index",
          title: "疫情安心卡"
        }, {
          path: "subpackages/split-coupons/list/index",
          title: "瓜分优惠券"
        }, {
          path: "subpackages/split-coupons/detail/index",
          title: "瓜分优惠券详情"
        }, {
          path: "subpackages/split-coupons/records/index",
          title: "瓜分优惠券记录"
        }, {
          path: "subpackages/queneUp/index",
          title: "取号"
        }, {
          path: "subpackages/queneUp/list",
          title: "我的取号"
        }, {
          path: "subpackages/queneUp/detail",
          title: "取号详情"
        }, {
          path: "pages/multi/list-instore",
          title: "堂食门店列表"
        }, {
          path: "pages/multi/choice-multi",
          title: "选择收货地址"
        }, {
          path: "pages/multi/list",
          title: "外卖门店列表"
        }, {
          path: "pages/multi/select-city",
          title: "选择城市"
        }, {
          path: "pages/multi/list-search",
          title: "搜索门店"
        }, {
          path: "pages/multi/list-component",
          title: "动态门店列表"
        }, {
          path: "pages/multi/youdian/search",
          title: "搜索"
        }, {
          path: "subpackages/protocol/index",
          title: "协议详情"
        }, {
          path: "subpackages/protocol/list/index",
          title: "我的协议"
        }, {
          path: "subpackages/protocol/detail/index",
          title: "协议详情"
        }, {
          path: "subpackages/protocol/privacy/recommend",
          title: "个性化推荐"
        }, {
          path: "subpackages/address/add/index",
          title: "添加地址"
        }, {
          path: "subpackages/address/list/index",
          title: "地址列表"
        }, {
          path: "subpackages/user-equity/level/index",
          title: "等级说明"
        }, {
          path: "subpackages/user-equity/index",
          title: "会员等级"
        }, {
          path: "subpackages/user-equity/level-record/index",
          title: "升降级记录"
        }, {
          path: "subpackages/user-equity/privilege-diff/index",
          title: "特权对比"
        }, {
          path: "subpackages/asset-merge/index",
          title: "合并资产"
        }, {
          path: "subpackages/asset-merge/merge/index",
          title: "合并资产"
        }, {
          path: "subpackages/asset-merge/unionid/index",
          title: "资产迁入"
        }, {
          path: "subpackages/bgImage/change-theme/index",
          title: "更换封面"
        }, {
          path: "subpackages/bgImage/choose-way/index",
          title: "更换主题"
        }, {
          path: "subpackages/bgImage/my-theme/index",
          title: "我的封面"
        }, {
          path: "subpackages/gift-card/index/index",
          title: "礼品卡列表"
        }, {
          path: "subpackages/gift-card/card/index",
          title: "购买礼品卡"
        }, {
          path: "subpackages/gift-card/confirm/index",
          title: "确认订单"
        }, {
          path: "subpackages/gift-card/exchange/index",
          title: "兑换礼品卡"
        }, {
          path: "subpackages/gift-card/details/index",
          title: "礼品卡详情"
        }, {
          path: "subpackages/gift-card/share-card/index",
          title: "赠送礼品卡"
        }, {
          path: "subpackages/gift-card/give/index",
          title: "赠送记录"
        }, {
          path: "subpackages/gift-card/record/index",
          title: "获卡记录"
        }, {
          path: "subpackages/gift-card/receive/index",
          title: "领取礼品卡"
        }, {
          path: "subpackages/gift-card/history/index",
          title: "历史礼品卡"
        }, {
          path: "subpackages/gift-card/notice/index",
          title: "礼品卡说明"
        }, {
          path: "subpackages/gift-card/orderDetail/index",
          title: "礼品卡订单详情"
        }, {
          path: "subpackages/gift-card/order-list/index",
          title: "礼品卡订单列表"
        }, {
          path: "subpackages/gift-card/rightsInterestsCard/index",
          title: "购买礼品卡"
        }, {
          path: "subpackages/gift-card/paySuccess/index",
          title: "礼品卡支付成功"
        }, {
          path: "subpackages/gift-card/batchGiftsCard/index",
          title: "赠送礼品卡"
        }, {
          path: "subpackages/gift-card/balance-transfer/index",
          title: "礼品卡余额转移"
        }, {
          path: "subpackages/gift-card/confirm-transfer/index",
          title: "礼品卡余额确认转移"
        }, {
          path: "subpackages/gift-card/physical-card/list",
          title: "实体储值卡列表"
        }, {
          path: "subpackages/gift-card/physical-card/record",
          title: "交易记录"
        }, {
          path: "subpackages/gift-card/apply-gift-cards/index",
          title: "适用礼品卡"
        }, {
          path: "subpackages/premium-membership/index/index",
          title: "付费权益卡"
        }, {
          path: "subpackages/premium-membership/rich-text/index",
          title: "权益卡说明"
        }, {
          path: "subpackages/premium-membership/buy-record/index",
          title: "付费权益卡购买记录"
        }, {
          path: "subpackages/premium-membership/select-cards/index",
          title: "可用付费卡优惠"
        }, {
          path: "subpackages/premium-membership/cover/index",
          title: "付费权益卡卡面管理"
        }, {
          path: "subpackages/premium-membership/give/index",
          title: "付费权益卡赠送好友"
        }, {
          path: "subpackages/premium-membership/receive/index",
          title: "领取付费权益卡"
        }, {
          path: "subpackages/premium-membership/exchange/index",
          title: "权益卡兑换"
        }, {
          path: "subpackages/premium-membership/collect/index",
          title: "权益卡领取"
        }, {
          path: "subpackages/premium-membership/my-cards/index",
          title: "我的权益卡列表"
        }, {
          path: "subpackages/premium-membership/student-certification/index",
          title: "学生认证页"
        }, {
          path: "subpackages/premium-membership/save-money-preview",
          title: "省钱攻略"
        }, {
          path: "subpackages/sign-in/index/index",
          title: "积分签到"
        }, {
          path: "subpackages/sign-in/rule/index",
          title: "积分签到规则"
        }, {
          path: "subpackages/value-card/agree-info/index",
          title: "储值规则"
        }, {
          path: "subpackages/value-card/balance-donate/index",
          title: "余额转赠"
        }, {
          path: "subpackages/value-card/balance-receive/index",
          title: "余额领取"
        }, {
          path: "subpackages/value-card/member-value/index",
          title: "会员储值"
        }, {
          path: "subpackages/value-card/notice/index",
          title: "使用须知"
        }, {
          path: "subpackages/value-card/pay-success/index",
          title: "会员储值支付成功"
        }, {
          path: "subpackages/value-card/record/index",
          title: "会员储值交易记录"
        }, {
          path: "subpackages/value-card/exchange/index",
          title: "储值兑换"
        }, {
          path: "subpackages/value-card/physical-card-recharge/index",
          title: "实体卡充值"
        }, {
          path: "subpackages/value-card/manage/index",
          title: "储值管理"
        }, {
          path: "subpackages/refund/refund-apply/index",
          title: "申请退款"
        }, {
          path: "subpackages/refund/refund-detail/index",
          title: "退款详情"
        }, {
          path: "subpackages/refund/refund-list/index",
          title: "退款记录"
        }, {
          path: "subpackages/refund/refund-content/index",
          title: "退款明细"
        }, {
          path: "subpackages/wishMatch/wishMatch",
          title: "套餐详情"
        }, {
          path: "subpackages/confirm/confirm",
          title: "确认订单"
        }, {
          path: "subpackages/detail/index",
          title: "订单详情"
        }, {
          path: "subpackages/evaluate/index/index",
          title: "评价"
        }, {
          path: "subpackages/evaluate/list/index",
          title: "我的评价"
        }, {
          path: "subpackages/evaluate/detail/index",
          title: "评价详情"
        }, {
          path: "subpackages/evaluate/add/index",
          title: "发表评价"
        }, {
          path: "subpackages/select-coupon/index",
          title: "可用优惠券"
        }, {
          path: "subpackages/coupon/promotion/index",
          title: "大促优惠券"
        }, {
          path: "subpackages/coupon/package/list/index",
          title: "券包列表"
        }, {
          path: "subpackages/coupon/package/detail/index",
          title: "券包详情"
        }, {
          path: "subpackages/coupon/package/record/index",
          title: "券包记录"
        }, {
          path: "subpackages/coupon/package/paySuccess/index",
          title: "券包购买成功"
        }, {
          path: "subpackages/coupon/voucher-coupon/index",
          title: "红包详情"
        }, {
          path: "subpackages/coupon/get-coupon/index",
          title: "领取优惠券"
        }, {
          path: "subpackages/coupon/exchange/index",
          title: "兑换优惠券"
        }, {
          path: "subpackages/coupon/get-activity/index",
          title: "领券中心"
        }, {
          path: "subpackages/coupon/package/agreeInfo/index",
          title: "付费券包协议"
        }, {
          path: "subpackages/coupon/tourist-coupon/index",
          title: "新人领券"
        }, {
          path: "subpackages/coupon/selected-goods/index",
          title: "券适用商品"
        }, {
          path: "subpackages/transform/index",
          title: "webView"
        }, {
          path: "subpackages/exchange-coupon/index",
          title: "兑换优惠券"
        }, {
          path: "pages/pay/success/index",
          title: "买单支付成功"
        }, {
          path: "pages/user/coupon/index",
          title: "我的优惠券"
        }, {
          path: "pages/user/info/info",
          title: "我的个人信息"
        }, {
          path: "subpackages/user/cancellation-cause/index",
          title: "注销原因"
        }, {
          path: "subpackages/user/cancellation-event/index",
          title: "确认注销事项"
        }, {
          path: "subpackages/user/account-security/index",
          title: "账号与安全"
        }, {
          path: "subpackages/user/cancellation/index",
          title: "账号注销协议"
        }, {
          path: "subpackages/user/agreement/index",
          title: "协议信息"
        }, {
          path: "subpackages/user/certification/index",
          title: "实名登记信息"
        }, {
          path: "subpackages/user/change-mobile/index",
          title: "切换账号"
        }, {
          path: "subpackages/user/update-mobile/index",
          title: "账号设置"
        }, {
          path: "subpackages/user/change-language/index",
          title: "语言设置"
        }, {
          path: "subpackages/user/areaCodeMobile/index",
          title: "选择地区"
        }, {
          path: "pages/coupon/coupon-receive/index",
          title: "优惠券领取"
        }, {
          path: "pages/coupon/user-coupon-stale/index",
          title: "历史优惠券"
        }, {
          path: "pages/coupon/user-giving-records/index",
          title: "优惠券赠送记录"
        }, {
          path: "pages/coupon/batch-coupons/index",
          title: "批量赠送优惠券"
        }, {
          path: "pages/coupon/customized-coupons/index",
          title: "定制优惠券"
        }, {
          path: "subpackages/invoice/index/index",
          title: "发票助手"
        }, {
          path: "subpackages/invoice/apply/index",
          title: "申请发票"
        }, {
          path: "subpackages/invoice/order-list/index",
          title: "可开票订单"
        }, {
          path: "subpackages/invoice/instructions/index",
          title: "开票须知"
        }, {
          path: "subpackages/pinDetails/pin-poster-edit",
          title: "好友拼单分享页"
        }, {
          path: "subpackages/pinDetails/index",
          title: "好友拼单页"
        }, {
          path: "subpackages/pinDetailsShare/index",
          title: "拼单详情"
        }, {
          path: "subpackages/suggestionFeedback/list/index",
          title: "建议反馈"
        }, {
          path: "subpackages/suggestionFeedback/add/index",
          title: "建议反馈"
        }, {
          path: "subpackages/marketing-detail/index",
          title: "营销活动详情"
        }, {
          path: "subpackages/familyMemberCard/index/index",
          title: "家庭会员卡"
        }, {
          path: "subpackages/familyMemberCard/cartManager/index",
          title: "家庭会员卡卡片管理"
        }, {
          path: "subpackages/familyMemberCard/addCard/index",
          title: "添加家庭会员卡"
        }, {
          path: "subpackages/familyMemberCard/cardSet/index",
          title: "家庭会员卡卡片管理"
        }, {
          path: "subpackages/third-equity/index/index",
          title: "三方权益"
        }, {
          path: "subpackages/third-equity/detail/index",
          title: "三方权益详情"
        }, {
          path: "subpackages/category-goods/index",
          title: "适用商品"
        }, {
          path: "subpackages/user-task-center/index/index",
          title: "任务中心"
        }, {
          path: "subpackages/user-task-center/record/index",
          title: "任务记录"
        }, {
          path: "subpackages/user-task-center/rule/index",
          title: "任务规则"
        }, {
          path: "subpackages/user-task-center/limitGoods/index",
          title: "任务中心-活动商品"
        }, {
          path: "subpackages/exchange-goods/index",
          title: "兑换商品"
        }, {
          path: "subpackages/exchange-goods/new-index",
          title: "兑换商品"
        }, {
          path: "subpackages/group-restaurant/address/list/index",
          title: "团餐地址列表"
        }, {
          path: "subpackages/group-restaurant/takefood/index",
          title: "团餐点单"
        }, {
          path: "subpackages/group-restaurant/confirm/index",
          title: "团餐下单"
        }, {
          path: "subpackages/group-restaurant/index/index",
          title: "团餐预定页"
        }, {
          path: "subpackages/group-restaurant/wishMatch/index",
          title: "团餐套餐详情"
        }, {
          path: "subpackages/group-restaurant/multi/choice-multi",
          title: "团餐选择地址"
        }, {
          path: "subpackages/group-restaurant/multi/list",
          title: "团餐外卖门店"
        }, {
          path: "subpackages/group-restaurant/multi/list-instore",
          title: "团餐堂食门店"
        }, {
          path: "subpackages/group-restaurant/multi/list-search",
          title: "团餐搜索门店"
        }, {
          path: "subpackages/group-purchase-coupon/list/index",
          title: "券列表"
        }, {
          path: "subpackages/group-purchase-coupon/ali-list/index",
          title: "支付宝团购券"
        }, {
          path: "subpackages/group-purchase-coupon/detail/index",
          title: "券详情"
        }, {
          path: "subpackages/group-purchase-coupon/cancel-coupon-helper/index",
          title: "团购兑换"
        }, {
          path: "subpackages/enterprise-wechat/customer/index",
          title: "门店客服"
        }, {
          path: "subpackages/enterprise-wechat/group-chat/index",
          title: "门店群聊"
        }, {
          path: "subpackages/lottery-reward/index",
          title: "领取详情"
        }, {
          path: "subpackages/lottery-reward/redirect",
          title: "领取详情"
        }, {
          path: "subpackages/lottery-reward/draw-down",
          title: "实物领取"
        }, {
          path: "subpackages/middlePage/multiple-person-ordering",
          title: "多人点单中间页"
        }, {
          path: "subpackages/login-auth/index",
          title: "登录授权页"
        }, {
          path: "subpackages/coupon-goods-list/index",
          title: "点单"
        }, {
          path: "subpackages/coupon-goods-list/multi-list",
          title: "选择门店"
        }, {
          path: "subpackages/coupon-goods-list/list",
          title: "选择门店"
        }, {
          path: "subpackages/site-pages/apply-goods/index",
          title: "适用商品"
        }, {
          path: "subpackages/site-pages/apply-stores/index",
          title: "适用门店"
        }, {
          path: "subpackages/site-pages/apply-rights-cards/index",
          title: "适用权益卡"
        }, {
          path: "subpackages/site-pages/search-goods/index",
          title: "商品搜索"
        }, {
          path: "subpackages/site-pages/password-setting/index",
          title: "密码设置"
        }, {
          path: "subpackages/site-pages/shopQqualification/index",
          title: "服务资质"
        }, {
          path: "subpackages/site-pages/pay-success/index",
          title: "会员码支付成功页"
        }, {
          path: "subpackages/site-pages/member-card-activation/index",
          title: "会员卡开卡"
        }, {
          path: "subpackages/site-pages/packaging-fee-detail/index",
          title: "包装费说明"
        }, {
          path: "subpackages/site-pages/no-queuing-privilege/index",
          title: "免排队特权"
        }, {
          path: "subpackages/site-pages/personalized-label/index",
          title: "个性化标签"
        }, {
          path: "subpackages/site-pages/personalized-label/edit",
          title: "创作杯贴"
        }, {
          path: "subpackages/site-pages/shop-home/index",
          title: "门店主页"
        }, {
          path: "subpackages/site-pages/shop/other-sell-shop/index",
          title: "商品售罄页"
        }, {
          path: "subpackages/site-pages/custom-web-view/index",
          title: "自定义web-view"
        }, {
          path: "subpackages/site-pages/pay/index",
          title: "支付中间页"
        }, {
          path: "subpackages/ai-order/index",
          title: "AI点单"
        }, {
          path: "subpackages/strongestDecibel/index/index",
          title: "最强分贝"
        }, {
          path: "subpackages/live-player/list/index",
          title: "直播大厅"
        }, {
          path: "plugins/index",
          title: "插件分包"
        }, {
          path: "plugins2/index",
          title: "插件分包2"
        }, {
          path: "subpackages/ar-cheers/index",
          title: "好朋友一直在一起"
        }]
      }, i.g.qmaiOpenPageRouteIdentifier = {}, i.g.currentSrcMode = "wx", i(1)
    },
    1: function (e, t, i) {
      "use strict";
      var n = {};
      i.r(n), i.d(n, {
        addPhoneContact: function () {
          return he
        },
        arrayBufferToBase64: function () {
          return ke
        },
        base64ToArrayBuffer: function () {
          return be
        },
        canvasGetImageData: function () {
          return Ie
        },
        canvasToTempFilePath: function () {
          return Te
        },
        checkSession: function () {
          return Ce
        },
        clearStorage: function () {
          return gt
        },
        clearStorageSync: function () {
          return ft
        },
        closeBLEConnection: function () {
          return Se
        },
        compressImage: function () {
          return Fe
        },
        connectSocket: function () {
          return rt
        },
        createAnimation: function () {
          return pe
        },
        createBLEConnection: function () {
          return xe
        },
        createInnerAudioContext: function () {
          return _e
        },
        createIntersectionObserver: function () {
          return Ae
        },
        createSelectorQuery: function () {
          return Ee
        },
        createVideoContext: function () {
          return Ot
        },
        downloadFile: function () {
          return qe
        },
        getClipboardData: function () {
          return Pe
        },
        getDeviceInfo: function () {
          return vt
        },
        getEnterOptionsSync: function () {
          return Et
        },
        getExtConfigSync: function () {
          return Rt
        },
        getNetworkType: function () {
          return Re
        },
        getScreenBrightness: function () {
          return it
        },
        getStorage: function () {
          return ct
        },
        getStorageInfo: function () {
          return ut
        },
        getStorageInfoSync: function () {
          return ht
        },
        getStorageSync: function () {
          return lt
        },
        getSystemInfo: function () {
          return mt
        },
        getSystemInfoSync: function () {
          return yt
        },
        getUserInfo: function () {
          return Ue
        },
        getWindowInfo: function () {
          return _t
        },
        hideLoading: function () {
          return Ct
        },
        hideTabBar: function () {
          return xt
        },
        hideToast: function () {
          return Tt
        },
        login: function () {
          return Le
        },
        makePhoneCall: function () {
          return Ge
        },
        navigateBack: function () {
          return Ye
        },
        navigateTo: function () {
          return $e
        },
        nextTick: function () {
          return He
        },
        offAppHide: function () {
          return ve
        },
        offAppShow: function () {
          return me
        },
        offError: function () {
          return ge
        },
        offNetworkStatusChange: function () {
          return De
        },
        offWindowResize: function () {
          return At
        },
        onAppHide: function () {
          return ye
        },
        onAppShow: function () {
          return fe
        },
        onBLEConnectionStateChange: function () {
          return we
        },
        onError: function () {
          return de
        },
        onNetworkStatusChange: function () {
          return Ne
        },
        onWindowResize: function () {
          return Pt
        },
        pageScrollTo: function () {
          return We
        },
        previewImage: function () {
          return je
        },
        reLaunch: function () {
          return Ze
        },
        redirectTo: function () {
          return Je
        },
        removeStorage: function () {
          return pt
        },
        removeStorageSync: function () {
          return dt
        },
        request: function () {
          return Ke
        },
        requestPayment: function () {
          return Qe
        },
        scanCode: function () {
          return et
        },
        setClipboardData: function () {
          return Oe
        },
        setNavigationBarColor: function () {
          return ot
        },
        setNavigationBarTitle: function () {
          return nt
        },
        setScreenBrightness: function () {
          return tt
        },
        setStorage: function () {
          return st
        },
        setStorageSync: function () {
          return at
        },
        setTabBarItem: function () {
          return bt
        },
        setTabBarStyle: function () {
          return kt
        },
        showActionSheet: function () {
          return ue
        },
        showLoading: function () {
          return It
        },
        showModal: function () {
          return Be
        },
        showTabBar: function () {
          return St
        },
        showToast: function () {
          return wt
        },
        startPullDownRefresh: function () {
          return ze
        },
        stopPullDownRefresh: function () {
          return Ve
        },
        switchTab: function () {
          return Xe
        },
        uploadFile: function () {
          return Me
        }
      });
      const o = e => {
        const t = [];
        return Object.entries(e).forEach(e => {
          let [i, n] = e;
          t.push("".concat(i, "=").concat(n))
        }), t.join("&")
      };
      let r;
      const s = () => {
          if (!r) throw Error("the mp sdk is not set");
          return r
        },
        a = {
          setStorage(e, t) {
            var i;
            return null === (i = r) || void 0 === i ? void 0 : i.setStorageSync(e, t)
          },
          getStorage(e) {
            var t;
            return null === (t = r) || void 0 === t ? void 0 : t.getStorageSync(e)
          },
          removeStorage(e) {
            var t;
            return null === (t = r) || void 0 === t ? void 0 : t.getStorageSync(e)
          }
        };

      function c(e) {
        return (c = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (e) {
          return typeof e
        } : function (e) {
          return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e
        })(e)
      }

      function l(e, t, i) {
        return (t = function (e) {
          var t = function (e) {
            if ("object" != c(e) || !e) return e;
            var t = e[Symbol.toPrimitive];
            if (void 0 !== t) {
              var i = t.call(e, "string");
              if ("object" != c(i)) return i;
              throw new TypeError("@@toPrimitive must return a primitive value.")
            }
            return String(e)
          }(e);
          return "symbol" == c(t) ? t : t + ""
        }(t)) in e ? Object.defineProperty(e, t, {
          value: i,
          enumerable: !0,
          configurable: !0,
          writable: !0
        }) : e[t] = i, e
      }

      function u() {
        return Math.random().toString(36).slice(2)
      }

      function h(e) {
        return Object.prototype.toString.call(e)
      }

      function p(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
      }

      function d(e) {
        return "[object BigInt]" === h(e)
      }

      function g(e) {
        return e instanceof Array
      }

      function f(e) {
        return "object" == typeof e && null !== e
      }

      function m(e) {
        return !(!f(e) || "[object Object]" !== h(e))
      }
      const y = e => "".concat(e),
        v = e => ({
          ok: !0,
          value: e
        });

      function _(e) {
        return void 0 === e ? v(y(e)) : null === e ? v(e) : function (e) {
          return "number" == typeof e
        }(e) && (e === -1 / 0 || e === 1 / 0 || Number.isNaN(e)) ? v(y(e)) : d(e) ? v("".concat(e, "n")) : "symbol" == typeof e || "function" == typeof e ? v(y(e.toString())) : e instanceof Error ? v(y(e.stack)) : e === Object.prototype ? {
          value: null,
          ok: !1
        } : e instanceof Object || "object" == typeof e ? {
          value: e,
          ok: !1
        } : v(e)
      }

      function b(e) {
        return void 0 === e ? "undefined" : null === e ? "null" : d(e) ? "bigint" : e instanceof Object ? e instanceof Error ? "error" : "function" == typeof e ? "function" : "object" : typeof e
      }
      const k = __spreadValues({}, console),
        S = ["log", "info", "error", "warn", "debug"].reduce((e, t) => (e[t] = function () {
          for (var e = arguments.length, i = new Array(e), n = 0; n < e; n++) i[n] = arguments[n];
          console[t]("[PageSpy] [".concat(t.toLocaleUpperCase(), "] "), ...i)
        }, e.unproxy[t] = function () {
          for (var e = arguments.length, i = new Array(e), n = 0; n < e; n++) i[n] = arguments[n];
          k[t]("[PageSpy] [".concat(t.toLocaleUpperCase(), "] "), ...i)
        }, e), {
          unproxy: {}
        }),
        x = "message",
        w = "broadcast",
        T = "ping",
        I = "updateRoomInfo";
      var C = Object.freeze({
        __proto__: null,
        BROADCAST: w,
        CLOSE: "close",
        CONNECT: "connect",
        ERROR: "error",
        JOIN: "join",
        LEAVE: "leave",
        MESSAGE: x,
        PING: T,
        PONG: "pong",
        UPDATE_ROOM_INFO: I
      });

      function O(e, t) {
        return {
          role: "client",
          type: e,
          data: __spreadValues(__spreadValues({}, (!(arguments.length > 2 && void 0 !== arguments[2]) || arguments[2]) && {
            id: u()
          }), t)
        }
      }
      class P {
        constructor() {
          l(this, "store", {}), l(this, "instanceStore", {})
        }
        getStore() {
          return this.store
        }
        resetStore() {
          this.store = {}
        }
        getInstanceStore() {
          return this.instanceStore
        }
        resetInstanceStore() {
          this.instanceStore = {}
        }
        transformToAtom(e) {
          const {
            value: t,
            ok: i
          } = _(e);
          return i ? {
            id: u(),
            type: b(e),
            value: t
          } : this.add(e)
        }
        get(e) {
          const t = this.store[e],
            i = this.instanceStore[e];
          if (!t) return null;
          const n = {},
            o = Object.getOwnPropertyDescriptors(t);
          Object.keys(o).forEach(e => {
            const t = o[e];
            p(t, "value") && (t.value = this.transformToAtom(t.value)), n[e] = P.getAtomOverview({
              atomId: u(),
              instanceId: i,
              value: t
            })
          });
          const r = this.addExtraProperty(e);
          return __spreadValues(__spreadValues({}, n), r)
        }
        getOrigin(e) {
          return this.store[e] || null
        }
        add(e) {
          let t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "";
          const i = u();
          let n = i;
          var o;
          f(o = e) && p(o, "constructor") && "function" == typeof o.constructor && (n = t), this.store[i] = e, this.instanceStore[i] = n;
          const r = P.getSemanticValue(e);
          return P.getAtomOverview({
            atomId: i,
            value: r,
            instanceId: n
          })
        }
        static getAtomOverview(e) {
          let {
            instanceId: t = "",
            atomId: i,
            value: n
          } = e;
          return {
            id: u(),
            type: "atom",
            __atomId: i,
            instanceId: t,
            value: n
          }
        }
        static getSemanticValue(e) {
          if (m(e)) return "Object {...}";
          if (g(e)) return "Array (".concat(e.length, ")");
          return e.constructor.name
        }
        addExtraProperty(e) {
          const t = this.store[e],
            i = this.instanceStore[e],
            n = {};
          if ((t instanceof String || t instanceof Number || t instanceof Boolean) && (n["[[PrimitiveValue]]"] = this.transformToAtom(t.valueOf())), t instanceof Set) {
            const e = {};
            let i = 0;
            for (const n of t) e[i++] = n;
            e.size = t.size, n["[[Entries]]"] = this.transformToAtom(e)
          }
          if (t instanceof Map) {
            const e = {};
            let i = 0;
            for (const [n, o] of t.entries()) e[i++] = {
              key: n,
              value: o
            };
            e.size = t.size, n["[[Entries]]"] = this.transformToAtom(e)
          }
          var o;
          return (g(t) || (o = t, "function" == typeof NodeList && "NodeList" === NodeList.name && o instanceof NodeList || "function" == typeof HTMLCollection && "HTMLCollection" === HTMLCollection.name && o instanceof HTMLCollection)) && (n.length = this.transformToAtom(t.length)), null !== Object.getPrototypeOf(t) ? n["[[Prototype]]"] = this.add(Object.getPrototypeOf(t), i) : n.___proto___ = this.transformToAtom(null), n
        }
      }
      var A = new P;
      const E = e => {
        let {
          osType: t,
          osVersion: i,
          browserType: n,
          browserVersion: o
        } = e;
        return "".concat(t, "/").concat(i, " ").concat(n, "/").concat(o)
      };
      class R {
        static makeClientInfoMsg() {
          const e = R.info.ua || E(R.info);
          return {
            sdk: R.info.sdk,
            isDevTools: R.info.isDevTools,
            ua: e,
            plugins: R.plugins
          }
        }
      }
      var N, D;
      l(R, "info", {
        osType: "unknown",
        osVersion: "unknown",
        browserType: "unknown",
        browserVersion: "unknown",
        framework: "unknown",
        isDevTools: !1,
        sdk: "browser"
      }), l(R, "plugins", []), (D = N || (N = {}))[D.CONNECTING = 0] = "CONNECTING", D[D.OPEN = 1] = "OPEN", D[D.CLOSING = 2] = "CLOSING", D[D.CLOSED = 3] = "CLOSED";
      const q = 2e3,
        M = Math.pow(1.5, 4) * q;
      class U {
        constructor() {
          l(this, "events", {
            open: [],
            close: [],
            error: [],
            message: []
          })
        }
        emit(e, t) {
          this.events[e].forEach(e => {
            e(t)
          }), "close" !== e && "error" !== e || this.clearListeners()
        }
        onOpen(e) {
          this.events.open.push(e)
        }
        onClose(e) {
          this.events.close.push(e)
        }
        onError(e) {
          this.events.error.push(e)
        }
        onMessage(e) {
          this.events.message.push(e)
        }
        clearListeners() {
          Object.entries(this.events).forEach(e => {
            let [, t] = e;
            t.splice(0)
          })
        }
      }
      class j {
        constructor() {
          l(this, "socketUrl", ""), l(this, "socketConnection", null), l(this, "debuggerConnection", null), l(this, "pingTimer", null), l(this, "pongTimer", null), l(this, "retryTimer", null), l(this, "isOffline", !1), l(this, "messageCapacity", 0), l(this, "messages", []), l(this, "events", {
            debug: [],
            refresh: [],
            "atom-detail": [],
            "atom-getter": [],
            "debugger-online": [],
            "database-pagination": [],
            "public-data": []
          }), l(this, "retryInterval", q), l(this, "connectable", !0), this.addListener("atom-detail", j.handleResolveAtom), this.addListener("atom-getter", j.handleAtomPropertyGetter), this.addListener("debugger-online", this.handleFlushBuffer)
        }
        init(e) {
          return __async(this, null, function* () {
            try {
              var t, i, n, o, r;
              if (!e) throw Error("WebSocket url cannot be empty");
              this.socketWrapper.clearListeners(), this.socketWrapper.getState() === N.OPEN && (yield new Promise(e => {
                this.socketWrapper.onClose(() => {
                  this.socketWrapper.clearListeners(), e()
                }), this.socketWrapper.close()
              })), null === (t = this.socketWrapper) || void 0 === t || t.onOpen(() => {
                this.connectOnline()
              }), null === (i = this.socketWrapper) || void 0 === i || i.onMessage(e => {
                this.handleMessage(e)
              }), null === (n = this.socketWrapper) || void 0 === n || n.onClose(() => {
                this.connectOffline()
              }), null === (o = this.socketWrapper) || void 0 === o || o.onError(() => {
                this.connectOffline()
              }), this.socketUrl = e, null === (r = this.socketWrapper) || void 0 === r || r.init(e)
            } catch (e) {
              S.error(e.message)
            }
          })
        }
        addListener(e, t) {
          this.events[e] || (this.events[e] = []), this.events[e].push(t)
        }
        broadcastMessage(e) {
          let t = arguments.length > 1 && void 0 !== arguments[1] && arguments[1];
          const i = function (e) {
            return {
              type: w,
              content: {
                data: e
              }
            }
          }(e);
          this.send(i, t)
        }
        close() {
          var e;
          this.connectable = !1, this.clearPing(), null === (e = this.socketWrapper) || void 0 === e || e.close(), this.messages = [], Object.entries(this.events).forEach(e => {
            let [t, i] = e;
            ["atom-detail", "atom-getter", "debugger-online"].includes(t) || i.splice(0)
          })
        }
        connectOnline() {
          this.retryInterval = q, this.updateRoomInfo(), this.ping()
        }
        connectOffline() {
          this.socketConnection = null, this.debuggerConnection = null, this.clearPing(), this.retryTimer && clearTimeout(this.retryTimer), this.connectable && (this.retryTimer = setTimeout(() => {
            this.retryInterval < M && (this.retryInterval *= 1.5), this.retryTimer = null, this.tryReconnect()
          }, this.retryInterval))
        }
        tryReconnect() {
          this.init(this.socketUrl)
        }
        ping() {
          this.pingTimer && clearTimeout(this.pingTimer), this.pongTimer && clearTimeout(this.pongTimer), this.pingTimer = setTimeout(() => {
            this.send({
              type: "ping",
              content: null
            }), this.pingTimer = null, this.pongTimer = setTimeout(() => {
              this.connectOffline(), this.pongTimer = null
            }, 5e3)
          }, 5e3)
        }
        clearPing() {
          this.pingTimer && (clearTimeout(this.pingTimer), this.pingTimer = null), this.pongTimer && (clearTimeout(this.pongTimer), this.pongTimer = null)
        }
        handlePong() {
          clearTimeout(this.pongTimer), this.pongTimer = null, this.ping()
        }
        handleMessage(e) {
          var t;
          j.messageFilters.length && j.messageFilters.forEach(t => {
            e = t(e)
          });
          const {
            CONNECT: i,
            MESSAGE: n,
            ERROR: o,
            JOIN: r,
            PING: s,
            PONG: a,
            LEAVE: c,
            CLOSE: l,
            BROADCAST: u
          } = C, h = JSON.parse(e.data), {
            type: p
          } = h;
          switch (p) {
            case i:
              const {
                selfConnection: e, roomConnections: s
              } = h.content;
              this.socketConnection = e, this.debuggerConnection = s.find(e => "Debugger" === e.userId) || null;
              break;
            case r:
            case c:
              const {
                connection: a
              } = h.content;
              "Debugger" === a.userId && (p === r ? (this.debuggerConnection = a, this.sendClientInfo()) : this.debuggerConnection = null);
              break;
            case n:
              const {
                data: u, from: d, to: g
              } = h.content;
              g.address === (null === (t = this.socketConnection) || void 0 === t ? void 0 : t.address) && this.dispatchEvent(u.type, {
                source: u,
                from: d,
                to: g
              });
              break;
            case l:
            case o:
              this.connectOffline()
          }
          this.handlePong()
        }
        dispatchEvent(e, t) {
          var i;
          ["public-data"].includes(e) ? this.events["public-data"].forEach(e => {
            e(t)
          }) : null === (i = this.events[e]) || void 0 === i || i.forEach(e => {
            e.call(this, t, e => {
              this.unicastMessage(e, t.from)
            })
          })
        }
        unicastMessage(e, t) {
          const i = function (e, t, i) {
            return {
              type: x,
              content: {
                data: e,
                from: t,
                to: i
              }
            }
          }(e, this.socketConnection, t);
          this.send(i)
        }
        handleFlushBuffer(e) {
          const {
            latestId: t
          } = e.source.data, i = this.messages.findIndex(e => e.content.data.data.id === t);
          this.messages.slice(i + 1).forEach(t => {
            const i = {
              type: x,
              content: {
                data: t.content.data,
                from: this.socketConnection,
                to: e.from
              }
            };
            this.send(i, !0)
          })
        }
        static handleResolveAtom(e, t) {
          let {
            source: i
          } = e;
          const {
            type: n,
            data: o
          } = i;
          if ("atom-detail" === n) {
            const e = A.get(o) || {};
            t(O("atom-detail-".concat(o), e, !1))
          }
        }
        static handleAtomPropertyGetter(e, t) {
          let {
            source: i
          } = e;
          const {
            type: n,
            data: o
          } = i;
          if ("atom-getter" === n) {
            const {
              id: e,
              parentId: i,
              key: n,
              instanceId: s
            } = o, a = A.getOrigin(s), c = A.getOrigin(i);
            let l = {};
            var r;
            l = a && c ? null === (r = Object.getOwnPropertyDescriptor(c, n)) || void 0 === r || null === (r = r.get) || void 0 === r ? void 0 : r.call(a) : new Error("Getter computed failed"), t(O("atom-getter-".concat(e), A.transformToAtom(l)))
          }
        }
        send(e) {
          let t = arguments.length > 1 && void 0 !== arguments[1] && arguments[1];
          if (this.checkIfSend(e)) try {
            var i;
            const t = e;
            t.createdAt = Date.now(), t.requestId = u();
            const n = function (e) {
              const {
                ok: t,
                value: i
              } = _(e);
              return t ? i : JSON.stringify(e, (e, t) => _(t).value, 2)
            }(t);
            null === (i = this.socketWrapper) || void 0 === i || i.send(n)
          } catch (e) {
            S.error("Incompatible: ".concat(e.message)), this.connectOffline()
          }
          this.checkIfCache(e, t) && (0 !== this.messageCapacity && this.messages.length >= this.messageCapacity && this.messages.shift(), this.messages.push(e))
        }
        checkIfSend(e) {
          return !(this.socketWrapper.getState() !== N.OPEN || ![I, T].includes(e.type) && !this.debuggerConnection)
        }
        checkIfCache(e) {
          let t = arguments.length > 1 && void 0 !== arguments[1] && arguments[1];
          return !this.isOffline && !t && ![x, T].includes(e.type)
        }
        sendClientInfo() {
          const e = R.makeClientInfoMsg();
          this.broadcastMessage({
            role: "client",
            type: "client-info",
            data: e
          }, !0)
        }
      }
      l(j, "messageFilters", []);
      const F = "page-spy-room";
      class L extends U {
        constructor() {
          super(...arguments), l(this, "socketInstance", null), l(this, "state", 0)
        }
        init(e) {
          return __async(this, null, function* () {
            this.state = N.CONNECTING;
            const t = s(),
              i = e => {
                this.state = N.CLOSED, this.emit("close", e)
              },
              n = e => {
                this.state = N.OPEN, this.emit("open", e)
              },
              o = e => {
                this.state = N.CLOSED, this.emit("error", e)
              },
              r = e => {
                this.emit("message", e)
              };
            if (L.isSingleSocket) t.connectSocket({
              url: e
            }), t.onSocketClose(i), t.onSocketError(o), t.onSocketMessage(r), t.onSocketOpen(n);
            else {
              let s = t.connectSocket({
                url: e,
                multiple: !0,
                complete() {}
              });
              s instanceof Promise && (s = yield s), s.onClose(i), s.onError(o), s.onOpen(n), s.onMessage(r), this.socketInstance = s
            }
          })
        }
        send(e) {
          var t;
          L.isSingleSocket ? s().sendSocketMessage({
            data: e
          }) : null === (t = this.socketInstance) || void 0 === t || t.send({
            data: e
          })
        }
        close() {
          var e;
          L.isSingleSocket ? s().closeSocket({}) : null === (e = this.socketInstance) || void 0 === e || e.close({}), this.state = N.CLOSED
        }
        getState() {
          return this.state
        }
      }
      l(L, "isSingleSocket", !1);
      var G, B = new class extends j {
        constructor() {
          super(...arguments), l(this, "socketWrapper", new L), l(this, "getPageSpyConfig", null)
        }
        updateRoomInfo() {
          if (this.getPageSpyConfig) {
            const {
              project: e,
              title: t
            } = this.getPageSpyConfig(), i = E(R.info);
            this.send({
              type: I,
              content: {
                info: {
                  name: i,
                  group: e,
                  tags: {
                    title: t,
                    name: i,
                    group: e
                  }
                }
              }
            }, !0)
          }
        }
        getSocket() {
          return this.socketWrapper
        }
        onOffline() {
          a.removeStorage(F)
        }
      };
      class H {
        constructor() {
          l(this, "name", "ConsolePlugin"), l(this, "console", {}), l(this, "proxyTypes", ["log", "info", "error", "warn", "debug"])
        }
        onInit() {
          return __async(this, null, function* () {
            if (H.hasInitd) return;
            H.hasInitd = !0;
            const e = this;
            this.proxyTypes.forEach(t => {
              this.console[t] = console[t] || console.log || (() => {}), Object.defineProperty(console, t, {
                value() {
                  const i = getCurrentPages().pop();
                  let n = "/";
                  i && (n = i.route, i.options && Object.keys(i.options).length > 0 && (n += "?" + o(i.options)));
                  for (var r = arguments.length, s = new Array(r), a = 0; a < r; a++) s[a] = arguments[a];
                  e.printLog({
                    logType: t,
                    logs: s,
                    url: n
                  })
                },
                configurable: !0,
                enumerable: !0,
                writable: !0
              })
            })
          })
        }
        onReset() {
          this.proxyTypes.forEach(e => {
            const t = this.console[e];
            t && (console[e] = t)
          }), H.hasInitd = !1
        }
        printLog(e) {
          if (e.logs && e.logs.length) {
            this.console[e.logType](...e.logs), e.logs = e.logs.map(e => A.transformToAtom(e));
            const t = O("console", __spreadValues({
              time: Date.now()
            }, e));
            B.dispatchEvent("public-data", t), B.broadcastMessage(t)
          }
        }
      }
      l(H, "hasInitd", !1);
      class W {
        constructor() {
          l(this, "name", "ErrorPlugin")
        }
        onInit() {
          W.hasInitd || (W.hasInitd = !0, this.onUncaughtError(), this.onUnhandledRejectionError())
        }
        onReset() {
          const e = s();
          e.canIUse("offError") && e.offError(this.errorHandler), e.canIUse("offUnHandledRejection") && e.offUnHandledRejection(this.unhandledRejectionHandler), W.hasInitd = !1
        }
        errorHandler(e) {
          if (W.hasInitd)
            if (e.stack || e.message) {
              const {
                message: t,
                stack: i
              } = e;
              W.sendMessage(i || t, (e => {
                if ("object" != typeof e) return null;
                const {
                  name: t,
                  message: i,
                  stack: n
                } = Object(e);
                return !1 === [t, i, n].every(Boolean) ? null : {
                  name: t,
                  message: i,
                  stack: n
                }
              })(e))
            } else {
              const e = "[PageSpy] An unknown error occurred and no message or stack trace available";
              W.sendMessage(e, null)
            }
        }
        unhandledRejectionHandler(e) {
          W.hasInitd && W.sendMessage("UnHandled Rejection", {
            name: "unhandledrejection",
            message: e.reason
          })
        }
        onUncaughtError() {
          const e = s();
          e.canIUse("onError") && e.onError(this.errorHandler)
        }
        onUnhandledRejectionError() {
          const e = s();
          e.canIUse("onUnHandledRejection") && e.onUnHandledRejection(this.unhandledRejectionHandler)
        }
        static sendMessage(e, t) {
          const i = O("console", {
            logType: "error",
            logs: [A.transformToAtom(e)],
            time: Date.now(),
            url: "wx:light-app",
            errorDetail: t
          });
          B.dispatchEvent("public-data", i), B.broadcastMessage(i)
        }
      }
      l(W, "hasInitd", !1),
        function (e) {
          e[e.UNSENT = 0] = "UNSENT", e[e.OPENED = 1] = "OPENED", e[e.HEADERS_RECEIVED = 2] = "HEADERS_RECEIVED", e[e.LOADING = 3] = "LOADING", e[e.DONE = 4] = "DONE"
        }(G || (G = {}));
      class V {
        constructor(e) {
          l(this, "id", ""), l(this, "name", ""), l(this, "method", ""), l(this, "url", ""), l(this, "requestType", "xhr"), l(this, "requestHeader", null), l(this, "status", 0), l(this, "statusText", ""), l(this, "readyState", 0), l(this, "responseReason", null), l(this, "responseType", ""), l(this, "responseHeader", null), l(this, "startTime", 0), l(this, "endTime", 0), l(this, "costTime", 0), l(this, "getData", null), l(this, "postData", null), l(this, "requestPayload", null), l(this, "withCredentials", !1), this.id = e
        }
      }
      class z {
        constructor(e) {
          l(this, "reqMap", Object.create(null)), this.socketStore = e
        }
        getRequestMap() {
          return this.reqMap
        }
        getRequest(e) {
          return this.reqMap[e]
        }
        removeRequest(e) {
          delete this.reqMap[e]
        }
        createRequest(e) {
          return e ? this.reqMap[e] ? (S.warn("The request object has been in store, disallow duplicate create"), !1) : (this.reqMap[e] = new V(e), !0) : (S.warn('The "id" is required when init request object'), !1)
        }
        setRequest(e, t) {
          return !(!e || !t || (this.reqMap[e] = t, 0))
        }
        sendRequestItem(e, t) {
          try {
            this.reqMap[e] || (this.reqMap[e] = t);
            const i = O("network", __spreadValues({}, t), !1);
            Number(t.readyState) === G.DONE && this.socketStore.dispatchEvent("public-data", i), this.socketStore.broadcastMessage(i, t.readyState !== G.DONE), this.deferDeleteRequest(e)
          } catch (e) {
            S.error(e.message)
          }
        }
        deferDeleteRequest(e) {
          const t = this.getRequest(e);
          t && t.readyState === G.DONE && setTimeout(() => {
            delete this.reqMap[e]
          }, 3e3)
        }
      }
      class K extends z {
        constructor() {
          super(B)
        }
      }
      class Q extends K {
        constructor() {
          super(), l(this, "request", null), this.initProxyHandler()
        }
        reset() {
          if (this.request) {
            const e = s();
            Object.defineProperty(e, "request", {
              value: this.request
            })
          }
        }
        initProxyHandler() {
          const e = this,
            t = s(),
            i = t.request;
          i && (this.request = i, Object.defineProperty(t, "request", {
            value(t) {
              const n = u();
              e.createRequest(n);
              const o = e.getRequest(n);
              if (o) {
                const r = t.method || "GET",
                  {
                    url: s
                  } = t;
                o.requestHeader = [];
                const a = function (e, t) {
                  try {
                    let i, n;
                    if ("object" == typeof window && "object" == typeof document && "[object HTMLDocument]" === Object.prototype.toString.call(document)) {
                      const {
                        searchParams: o,
                        href: r
                      } = new URL(e, t);
                      i = r, n = [...o.entries()]
                    } else i = e.toString(), n = function (e) {
                      const t = /[?&]([^=#]+)=([^&#]*)/g,
                        i = [];
                      let n;
                      for (; null !== (n = t.exec(e));) {
                        const e = decodeURIComponent(n[1]),
                          t = decodeURIComponent(n[2]);
                        i.push([e, t])
                      }
                      return i
                    }(i);
                    const o = i.replace(/^.*?([^/]+)(\/)*(\?.*?)?$/, "$1$2$3") || "";
                    return {
                      url: i,
                      name: o,
                      query: n
                    }
                  } catch (e) {
                    return {
                      url: "Unknown",
                      name: "Unknown",
                      query: null
                    }
                  }
                }(s);
                if (o.url = a.url, o.name = a.name, o.getData = a.query, o.method = r.toUpperCase(), o.requestType = "mp-request", o.status = 0, o.statusText = "Pending", o.startTime = Date.now(), o.readyState = G.UNSENT, m(t.header) && (o.requestHeader = Object.entries(t.header).map(e => {
                    let [t, i] = e;
                    return [String(t), String(i)]
                  })), "GET" !== o.method) {
                  o.requestHeader.push(["Content-Type", "application/json"]);
                  const {
                    data: e
                  } = t;
                  if (e)
                    if ("string" == typeof e) o.requestPayload = e;
                    else if (e instanceof ArrayBuffer) o.requestPayload = "[object ArrayBuffer]";
                  else try {
                    o.requestPayload = JSON.stringify(e)
                  } catch (t) {
                    o.requestPayload = h(e)
                  }
                }
                e.sendRequestItem(n, o);
                const c = t.success,
                  l = t.fail,
                  u = t.complete,
                  p = () => {
                    o.endTime = Date.now(), o.costTime = o.endTime - (o.startTime || o.endTime)
                  },
                  d = function (t) {
                    p(), o.status = (null == t ? void 0 : t.statusCode) || 200, o.statusText = "Done", o.responseHeader = [...Object.entries((null == t ? void 0 : t.header) || {})], o.readyState = G.HEADERS_RECEIVED, e.sendRequestItem(n, o);
                    const i = function (e) {
                      const t = Object.keys(e),
                        i = {};
                      for (let n = 0; n < t.length; n++) {
                        const o = t[n];
                        i[o.toLowerCase()] = e[o]
                      }
                      return i
                    }((null == t ? void 0 : t.header) || {})["content-type"];
                    switch (i && (i.includes("application/json") && (o.responseType = "json"), (i.includes("text/html") || i.includes("text/plain")) && (o.responseType = "text")), o.responseType || (o.responseType = "arraybuffer"), o.responseType) {
                      case "json":
                      case "text":
                        if ("string" == typeof (null == t ? void 0 : t.data)) try {
                          o.response = JSON.parse(t.data)
                        } catch (e) {
                          o.response = t.data, o.responseType = "text"
                        } else o.response = null == t ? void 0 : t.data;
                        break;
                      case "arraybuffer":
                        o.response = "[object ArrayBuffer]"
                    }
                  },
                  g = function () {
                    p()
                  },
                  f = function () {
                    o.readyState = G.DONE, e.sendRequestItem(n, o)
                  };
                if (c || l) return t.success = function (e) {
                  d(e), null == c || c(e)
                }, t.fail = function (e) {
                  g(), null == l || l(e)
                }, t.complete = function (e) {
                  f(), null == u || u(e)
                }, i(t);
                const y = i(t);
                return y.then(e => {
                  d(e)
                }), y.catch(() => {
                  g()
                }), y.finally(() => {
                  f()
                }), y
              }
              return S.warn("The request object is not found on request event"), null
            }
          }))
        }
      }
      class J {
        constructor() {
          l(this, "name", "NetworkPlugin"), l(this, "requestProxy", null)
        }
        onInit() {
          J.hasInitd || (J.hasInitd = !0, this.requestProxy = new Q)
        }
        onReset() {
          var e;
          null === (e = this.requestProxy) || void 0 === e || e.reset(), J.hasInitd = !1
        }
      }
      l(J, "hasInitd", !1);
      class $ {
        constructor() {
          l(this, "name", "SystemPlugin")
        }
        onInit() {
          $.hasInitd || ($.hasInitd = !0, B.addListener("refresh", (e, t) => {
            let {
              source: i
            } = e;
            const {
              data: n
            } = i;
            if ("system" === n) {
              const e = $.getSystemInfo();
              B.dispatchEvent("public-data", e), t(e)
            }
          }))
        }
        onReset() {
          $.hasInitd = !1
        }
        static getSystemInfo() {
          const e = R.info;
          return O("system", {
            system: {
              ua: E(e)
            },
            features: {}
          })
        }
      }

      function Y(e) {
        const t = typeof e;
        let i = e;
        return "string" === t || "boolean" === t || "number" === t ? i = String(e) : "object" === t && (i = e instanceof Date ? e.toDateString() : JSON.stringify(e)), i
      }
      l($, "hasInitd", !1);
      class Z {
        constructor() {
          l(this, "name", "StoragePlugin")
        }
        onInit() {
          Z.hasInitd || (Z.hasInitd = !0, Z.initStorageProxy(), Z.listenRefreshEvent())
        }
        onReset() {
          const e = s();
          Object.entries(Z.originFunctions).forEach(t => {
            let [i, n] = t;
            Object.defineProperty(e, i, {
              value: n
            })
          }), Z.hasInitd = !1
        }
        static sendRefresh() {
          const e = s();
          try {
            const t = {
              type: "mpStorage",
              action: "get",
              data: e.getStorageInfoSync().keys.map(e => ({
                name: e,
                value: Y(a.getStorage(e))
              }))
            };
            Z.sendStorageItem(t)
          } catch (e) {}
        }
        static listenRefreshEvent() {
          B.addListener("refresh", e => __async(null, null, function* () {
            let {
              source: t
            } = e;
            const {
              data: i
            } = t;
            "mpStorage" === i && Z.sendRefresh()
          }))
        }
        static initStorageProxy() {
          const e = s(),
            {
              sendClearItem: t,
              sendRemoveItem: i,
              sendSetItem: n
            } = Z;
          ["setStorage", "setStorageSync", "removeStorage", "removeStorageSync", "clearStorage", "clearStorageSync", "batchSetStorageSync", "batchSetStorage"].forEach(t => {
            e[t] && (Z.originFunctions[t] = e[t])
          }), Object.defineProperties(e, {
            setStorage: {
              value: e => Z.originFunctions.setStorage(__spreadProps(__spreadValues({}, e), {
                success(t) {
                  var i;
                  n(e.key, e.data), null === (i = e.success) || void 0 === i || i.call(e, t)
                }
              }))
            },
            setStorageSync: {
              value(e, t) {
                try {
                  let i;
                  if ("mp-alipay" !== R.info.browserType || R.info.framework && "unknown" !== R.info.framework) {
                    const o = e;
                    i = Z.originFunctions.setStorageSync(o, t), n(o, t)
                  } else {
                    const t = e;
                    i = Z.originFunctions.setStorageSync(t), n(t.key, t.data)
                  }
                  return i
                } catch (t) {
                  throw S.error("Failed to set storage synchronously: ".concat(e)), t
                }
              }
            },
            removeStorage: {
              value: e => Z.originFunctions.removeStorage(__spreadProps(__spreadValues({}, e), {
                success(t) {
                  var n;
                  i(e.key), null === (n = e.success) || void 0 === n || n.call(e, t)
                }
              }))
            },
            removeStorageSync: {
              value(e) {
                try {
                  const t = Z.originFunctions.removeStorageSync(e);
                  return i(t), t
                } catch (t) {
                  throw S.error("Failed to remove storage synchronously: ".concat(e)), t
                }
              }
            },
            clearStorage: {
              value: e => Z.originFunctions.clearStorage(__spreadProps(__spreadValues({}, e), {
                success(i) {
                  var n;
                  t(), null === (n = e.success) || void 0 === n || n.call(e, i)
                }
              }))
            },
            clearStorageSync: {
              value() {
                try {
                  const e = Z.originFunctions.clearStorageSync();
                  return t(), e
                } catch (e) {
                  throw S.error("Failed to clear storage synchronously"), e
                }
              }
            }
          }), e.canIUse("batchSetStorageSync") && Object.defineProperty(e, "batchSetStorageSync", {
            value(e) {
              try {
                const t = Z.originFunctions.batchSetStorageSync(e);
                return e.forEach(e => {
                  n(e.key, e.value)
                }), t
              } catch (t) {
                throw S.error("Failed to batch set storage synchronously: ".concat(JSON.stringify(e.map(e => e.key)))), t
              }
            }
          }), e.canIUse("batchSetStorage") && Object.defineProperty(e, "batchSetStorage", {
            value: e => Z.originFunctions.batchSetStorage(__spreadProps(__spreadValues({}, e), {
              success(t) {
                var i;
                e.kvList.forEach(e => {
                  n(e.key, e.value)
                }), null === (i = e.success) || void 0 === i || i.call(e, t)
              }
            }))
          })
        }
        static sendSetItem(e, t) {
          Z.sendStorageItem({
            type: "mpStorage",
            action: "set",
            name: e,
            value: Y(t)
          })
        }
        static sendRemoveItem(e) {
          Z.sendStorageItem({
            type: "mpStorage",
            action: "remove",
            name: e
          })
        }
        static sendClearItem() {
          Z.sendStorageItem({
            type: "mpStorage",
            action: "clear"
          })
        }
        static sendStorageItem(e) {
          const t = O("storage", e);
          B.dispatchEvent("public-data", t), B.broadcastMessage(t, !0)
        }
      }
      l(Z, "hasInitd", !1), l(Z, "originFunctions", {});
      const X = e => !1 === e ? ["http://", "ws://"] : ["https://", "wss://"];
      class ee {
        constructor(e) {
          if (this.config = e, !e.get().api) throw Error("The api base url cannot be empty")
        }
        get base() {
          return this.config.get().api
        }
        createRoom() {
          const {
            enableSSL: e,
            project: t,
            title: i,
            useSecret: n,
            secret: r
          } = this.config.get(), a = X(e), c = E(R.info), l = o({
            group: t,
            title: i,
            name: encodeURIComponent(c)
          });
          return (u = s().request, e => new Promise((t, i) => {
            u(__spreadProps(__spreadValues({}, e), {
              success(e) {
                t(e)
              },
              fail(e) {
                i(e)
              }
            }))
          }))({
            url: "".concat(a[0]).concat(this.base, "/api/v1/room/create?").concat(l),
            method: "POST",
            data: JSON.stringify({
              useSecret: n,
              secret: r
            })
          }).then(e => {
            var t;
            const {
              name: i,
              address: n
            } = (null === (t = e.data) || void 0 === t ? void 0 : t.data) || {};
            return {
              roomUrl: this.getRoomUrl(n),
              address: n,
              name: i
            }
          }, e => {
            throw Error("Request create room failed: ".concat(e.message))
          });
          var u
        }
        getRoomUrl(e) {
          const t = this.config.get(),
            i = X(t.enableSSL);
          return "".concat(i[1]).concat(this.base, "/api/v1/ws/room/join?").concat(o({
            address: e,
            name: "client:".concat(u()),
            userId: "Client",
            forceCreate: !0,
            useSecret: t.useSecret,
            secret: t.secret
          }))
        }
      }
      class te {
        defaultConfig() {
          return {}
        }
        constructor() {
          l(this, "mergeConfig", e => {
            const t = Object.entries(e).reduce((e, t) => {
              let [i, n] = t;
              return this.privateKeys.includes(i) || (e[i] = n), e
            }, {});
            return this.value = __spreadValues(__spreadValues({}, this.defaultConfig()), t), this.value
          }), this.value = this.defaultConfig()
        }
        get() {
          return this.value
        }
        set(e, t) {
          this.value[e] = t
        }
      }
      class ie extends te {
        constructor() {
          super(...arguments), l(this, "privateKeys", ["secret"])
        }
        defaultConfig() {
          return {
            api: "",
            project: "default",
            title: "",
            enableSSL: null,
            disabledOnProd: !0,
            disabledPlugins: [],
            singletonSocket: !1,
            messageCapacity: 1e3,
            useSecret: !1,
            secret: ""
          }
        }
      }
      class ne {
        constructor(e) {
          if (l(this, "root", null), l(this, "version", "1.0.54"), l(this, "request", null), l(this, "name", ""), l(this, "address", ""), l(this, "roomUrl", ""), l(this, "socketStore", B), l(this, "config", new ie), l(this, "cacheTimer", null), ne.instance) return S.warn("Cannot initialize PageSpy multiple times"), ne.instance;
          const t = this.config.mergeConfig(e);
          t.singletonSocket && (L.isSingleSocket = !0);
          const i = s();
          if (i.canIUse("getAccountInfoSync") && "release" === i.getAccountInfoSync().miniProgram.envVersion && !1 !== t.disabledOnProd) return void S.warn("PageSpy is not allowed on release env of mini program");
          ne.instance = this, this.request = new ee(this.config), this.updateConfiguration(), this.triggerPlugins("onInit", {
            socketStore: B,
            config: t
          }), R.plugins = ne.pluginsWithOrder.map(e => e.name), this.init()
        }
        updateConfiguration() {
          const {
            messageCapacity: e,
            useSecret: t
          } = this.config.get();
          if (!0 === t) {
            const e = a.getStorage(F),
              t = (null == e ? void 0 : e.secret) || function () {
                const e = Math.floor(1e6 * Math.random());
                return String(e).padStart(6, "0")
              }();
            this.config.set("secret", t), S.log("Room Secret: ".concat(t))
          }
          B.connectable = !0, B.getPageSpyConfig = () => this.config.get(), B.messageCapacity = e
        }
        init() {
          return __async(this, null, function* () {
            const e = s(),
              t = this.config.get(),
              i = a.getStorage(F);
            if (i && "object" == typeof i) {
              const {
                name: e,
                address: n,
                roomUrl: o,
                project: r
              } = i;
              t.project !== r ? yield this.createNewConnection(): (this.name = e, this.address = n, this.roomUrl = o, this.useOldConnection())
            } else yield this.createNewConnection();
            e.canIUse("onAppShow") && e.onAppShow(() => {
              const e = B.getSocket().getState();
              e !== N.CLOSED && e !== N.CLOSING || this.useOldConnection()
            }), S.log("Plugins inited")
          })
        }
        createNewConnection() {
          return __async(this, null, function* () {
            if (!this.request) return void S.error("Cannot get the Request");
            const e = yield this.request.createRoom();
            this.name = e.name, this.address = e.address, this.roomUrl = e.roomUrl, this.refreshRoomInfo(), B.init(e.roomUrl)
          })
        }
        useOldConnection() {
          this.refreshRoomInfo(), B.init(this.roomUrl)
        }
        refreshRoomInfo() {
          this.saveSession(), this.cacheTimer = setInterval(() => {
            B.getSocket().getState() === N.OPEN && this.saveSession()
          }, 15e3), S.log("Room ID: ".concat(this.address.slice(0, 4)))
        }
        saveSession() {
          const {
            name: e,
            address: t,
            roomUrl: i,
            config: n
          } = this, {
            useSecret: o,
            secret: r,
            project: s
          } = n.get(), c = {
            name: e,
            address: t,
            roomUrl: i,
            project: s,
            useSecret: o,
            secret: r
          };
          a.setStorage(F, c)
        }
        triggerPlugins(e) {
          for (var t = arguments.length, i = new Array(t > 1 ? t - 1 : 0), n = 1; n < t; n++) i[n - 1] = arguments[n];
          const {
            disabledPlugins: o
          } = this.config.get();
          ne.pluginsWithOrder.forEach(t => {
            var n;
            g(o) && o.length && o.includes(t.name) || null === (n = t[e]) || void 0 === n || n.apply(t, i)
          })
        }
        abort() {
          this.triggerPlugins("onReset"), B.close(), ne.instance = null
        }
        updateRoomInfo(e) {
          if (!e) return;
          const {
            project: t,
            title: i
          } = e;
          t && this.config.set("project", String(t)), i && this.config.set("title", String(i)), B.updateRoomInfo()
        }
        static get pluginsWithOrder() {
          return [...ne.plugins.pre, ...ne.plugins.normal, ...ne.plugins.post]
        }
        static registerPlugin(e) {
          if (!e) return;
          if ("function" == typeof (t = e) && void 0 !== t.prototype) return void S.error("PageSpy.registerPlugin() expect to pass an instance, not a class");
          var t;
          if (!e.name) return void S.error("The ".concat(e.constructor.name, ' plugin should provide a "name" property'));
          if (ne.pluginsWithOrder.some(t => t.name === e.name)) return void S.error("The ".concat(e.name, ' has registered. Consider the following reasons:\n      - Duplicate register one same plugin;\n      - Plugin\'s "name" conflict with others, you can print all registered plugins by "PageSpy.plugins";'));
          ne.plugins[e.enforce || "normal"].push(e)
        }
      }

      function oe(e) {
        try {
          return e.getExtConfigSync().appVersion || ""
        } catch (t) {
          try {
            const {
              miniProgram: t
            } = e.getAccountInfoSync();
            return "".concat({
              release: "正式版",
              trial: "体验版",
              develop: "开发版"
            } [t.envVersion], " ").concat(t.version)
          } catch (e) {}
        }
        return "暂无"
      }
      l(ne, "instance", null), l(ne, "plugins", {
        pre: [],
        normal: [],
        post: []
      }), [new H, new W, new J, new Z, new $].forEach(e => {
        ne.registerPlugin(e)
      });
      let re = "";
      re = "新饮食小程序",
        function (e, t) {
          try {
            let n;
            n = t || wx;
            if (function (e) {
                try {
                  0;
                  const t = e.getAccountInfoSync();
                  return !("trial" === t.miniProgram.envVersion || "develop" === t.miniProgram.envVersion)
                } catch (e) {}
                return !0
              }(n)) return void S.log("正式版不启用");
            const o = "pagespy.qmai.cn",
              {
                project: s,
                app: c
              } = e,
              l = "生产环境";
            r = n;
            const u = n.getSystemInfoSync();
            let h = "unknown",
              p = "unknown",
              d = "unknown",
              g = "unknown";
            h = {
              wx: "mp-wechat",
              ali: "mp-alipay",
              tt: "mp-douyin",
              qq: "mp-qq",
              swan: "mp-baidu"
            }.wx || "unknown"; {
              var i;
              const e = null === (i = u.system) || void 0 === i ? void 0 : i.split(" ");
              d = (null == e ? void 0 : e[0].toLowerCase()) || "unknown", g = (null == e ? void 0 : e[1].toLowerCase()) || "unknown", p = u.version
            }
            if (R.info = {
                framework: "uniapp",
                sdk: "uniapp",
                osType: d,
                osVersion: g,
                browserType: h,
                browserVersion: p,
                isDevTools: "devtools" === u.platform
              }, R.info.isDevTools && !0 !== a.getStorage("enable-page-spy")) return void S.log("在开发者工具上默认不启用, 因为劫持 console 会导致无法定位到具体代码行, 可在控制台执行 wx.setStorageSync('enable-page-spy', true) 启用");
            ! function (e, t, i) {
              try {
                const n = t.address.slice(0, 4);
                if (!n) return;
                let o = !1;
                e.startAccelerometer({
                  interval: "normal"
                });
                const r = t => {
                  if (t.x > 1 && !1 === o) {
                    o = !0;
                    const t = "远程调试房间号: ".concat(n);
                    e.showModal({
                      title: i.project + "(" + i.title + ")",
                      content: t + "\n小程序版本号: " + oe(e) + "\n 应用: " + i.app,
                      confirmText: "我知道了",
                      confirmColor: "#8235E4",
                      showCancel: !1,
                      complete: () => {
                        e.offAccelerometerChange(r), e.stopAccelerometer()
                      }
                    })
                  }
                };
                e.onAccelerometerChange(r)
              } catch (e) {}
            }(n, new ne({
              api: o,
              project: s,
              title: l
            }), {
              project: s,
              title: l,
              app: c
            })
          } catch (e) {
            S.error(e)
          }
        }({
          project: re,
          app: "catering"
        });
      var se = i(2),
        ae = i(3);

      function ce(e) {
        return () => {
          throw Error("[@mpxjs/api-proxy error]:\n ".concat("wx", "环境不支持").concat(e, "方法"))
        }
      }
      const le = (0, ae.l)(),
        ue = le.showActionSheet || ce("showActionSheet"),
        he = le.addPhoneContact || ce("addPhoneContact"),
        pe = le.createAnimation || ce("createAnimation"),
        de = le.onError || ce("onError"),
        ge = le.offError || ce("offError"),
        fe = le.onAppShow || ce("onAppShow"),
        me = le.offAppShow || ce("offAppShow"),
        ye = le.onAppHide || ce("onAppHide"),
        ve = le.offAppHide || ce("offAppHide"),
        _e = le.createInnerAudioContext || ce("createInnerAudioContext"),
        be = le.base64ToArrayBuffer || ce("base64ToArrayBuffer"),
        ke = le.arrayBufferToBase64 || ce("arrayBufferToBase64"),
        Se = le.closeBLEConnection || ce("closeBLEConnection"),
        xe = le.createBLEConnection || ce("createBLEConnection"),
        we = le.onBLEConnectionStateChange || ce("onBLEConnectionStateChange"),
        Te = le.canvasToTempFilePath || ce("canvasToTempFilePath"),
        Ie = le.canvasGetImageData || ce("canvasGetImageData"),
        Ce = le.checkSession || ce("checkSession"),
        Oe = le.setClipboardData || ce("setClipboardData"),
        Pe = le.getClipboardData || ce("getClipboardData"),
        Ae = le.createIntersectionObserver || ce("createIntersectionObserver"),
        Ee = le.createSelectorQuery || ce("createSelectorQuery"),
        Re = le.getNetworkType || ce("getNetworkType"),
        Ne = le.onNetworkStatusChange || ce("onNetworkStatusChange"),
        De = le.offNetworkStatusChange || ce("offNetworkStatusChange"),
        qe = le.downloadFile || ce("downloadFile"),
        Me = le.uploadFile || ce("uploadFile"),
        Ue = le.getUserInfo || ce("getUserInfo"),
        je = le.previewImage || ce("previewImage"),
        Fe = le.compressImage || ce("compressImage"),
        Le = le.login || ce("login"),
        Ge = le.makePhoneCall || ce("makePhoneCall");

      function Be(e = {}) {
        const t = e.fail,
          i = e.success;
        e.success = function (e) {
          e.confirm ? i.call(this, e) : t.call(this)
        }, le.showModal(e)
      }
      const He = le.nextTick || ce("nextTick"),
        We = le.pageScrollTo || ce("pageScrollTo"),
        Ve = le.stopPullDownRefresh || ce("stopPullDownRefresh"),
        ze = le.startPullDownRefresh || ce("startPullDownRefresh"),
        Ke = le.request || ce("request"),
        Qe = le.requestPayment || ce("requestPayment"),
        Je = le.redirectTo || ce("redirectTo"),
        $e = le.navigateTo || ce("navigateTo"),
        Ye = le.navigateBack || ce("navigateBack"),
        Ze = le.reLaunch || ce("reLaunch"),
        Xe = le.switchTab || ce("switchTab"),
        et = le.scanCode || ce("scanCode"),
        tt = le.setScreenBrightness || ce("setScreenBrightness"),
        it = le.getScreenBrightness || ce("getScreenBrightness"),
        nt = le.setNavigationBarTitle || ce("setNavigationBarTitle"),
        ot = le.setNavigationBarColor || ce("setNavigationBarColor"),
        rt = le.connectSocket || ce("connectSocket"),
        st = le.setStorage || ce("setStorage"),
        at = le.setStorageSync || ce("setStorageSync"),
        ct = le.getStorage || ce("getStorage"),
        lt = le.getStorageSync || ce("getStorageSync"),
        ut = le.getStorageInfo || ce("getStorageInfo"),
        ht = le.getStorageInfoSync || ce("getStorageInfoSync"),
        pt = le.removeStorage || ce("removeStorage"),
        dt = le.removeStorageSync || ce("removeStorageSync"),
        gt = le.clearStorage || ce("clearStorage"),
        ft = le.clearStorageSync || ce("clearStorageSync"),
        mt = le.getSystemInfo || ce("getSystemInfo"),
        yt = le.getSystemInfoSync || ce("getSystemInfoSync"),
        vt = le.getDeviceInfo || ce("getDeviceInfo"),
        _t = le.getWindowInfo || ce("getWindowInfo"),
        bt = le.setTabBarItem || ce("setTabBarItem"),
        kt = le.setTabBarStyle || ce("setTabBarStyle"),
        St = le.showTabBar || ce("showTabBar"),
        xt = le.hideTabBar || ce("hideTabBar");

      function wt(e = {}) {
        e.icon || (e.icon = "none"), e.title && le.showToast(e)
      }
      const Tt = le.hideToast || ce("hideToast"),
        It = le.showLoading || ce("showLoading"),
        Ct = le.hideLoading || ce("hideLoading"),
        Ot = le.createVideoContext || ce("createVideoContext"),
        Pt = le.onWindowResize || ce("onWindowResize"),
        At = le.offWindowResize || ce("offWindowResize"),
        Et = le.getEnterOptionsSync || ce("getEnterOptionsSync"),
        Rt = le.getExtConfigSync || ce("getExtConfigSync"),
        Nt = ["clearStorage", "hideToast", "hideLoading", "drawCanvas", "canIUse", "stopRecord", "pauseVoice", "stopVoice", "pauseBackgroundAudio", "stopBackgroundAudio", "showNavigationBarLoading", "hideNavigationBarLoading", "createAnimation", "createAnimationVideo", "createSelectorQuery", "createIntersectionObserver", "getPerformance", "hideKeyboard", "stopPullDownRefresh", "createWorker", "pageScrollTo", "reportAnalytics", "getMenuButtonBoundingClientRect", "reportMonitor", "createOffscreenCanvas", "reportEvent", "connectSocket", "base64ToArrayBuffer"];

      function Dt(e) {
        if (e && e.length) {
          const t = {};
          return e.forEach(e => {
            t[e] = !0
          }), t
        }
      }
      var qt = function (e, t, i) {
        const n = {},
          o = Dt(t),
          r = Dt(Nt.concat(i));
        return Object.keys(e).forEach(t => {
          if ("function" != typeof e[t]) return;
          n[t] = function (...i) {
            const n = i[0] || {};
            if (! function (e) {
                return o && void 0 !== o[e] ? !!o[e] : !(r[e] || /^get\w*Manager$/.test(e) || /^create\w*Context$/.test(e) || /^(on|off)/.test(e) || /\w+Sync$/.test(e))
              }(t) || n.success || n.fail) return e[t].apply(le, i); {
              let o;
              i[0] || i.unshift(n);
              const r = new Promise((r, s) => {
                n.success = r, n.fail = s, o = e[t].apply(le, i)
              });
              return r.__returned = o, r
            }
          }
        }), n
      };

      function Mt(e, t = {}) {
        const {
          usePromise: i = !1,
          whiteList: o = [],
          blackList: r = [],
          custom: s = {}
        } = t, a = Object.assign({}, le, n), c = i ? qt(a, o, r) : {};
        Object.assign(e, a, c, s.wx)
      }
      var Ut = Mt,
        jt = i(32);
      se.a.use(Ut, {
        usePromise: !0
      }); {
        const e = (...e) => console.log("[qmai-performance]", ...e),
          t = wx.getPerformance && wx.getPerformance() || null;
        if (t && t.createObserver) {
          let n = 0,
            o = 0,
            r = 0,
            s = 0,
            a = 0,
            c = "",
            l = "",
            u = "",
            h = 0,
            p = 0,
            d = 0;
          t.createObserver(t => {
            var g;
            const f = [];
            if (t.getEntries().forEach(t => {
                f.push(t);
                const i = parseInt(t.duration, 10);
                c = t.name || "", l = t.path || "", "loadPackage" === t.entryType && "downloadPackage" === t.name ? (u = t.packageName || "", p = t.packageSize, h = i || 0, "__APP__" === t.packageName ? e("主包大小".concat(parseInt(t.packageSize, 10), ", 下载耗时").concat(i, "ms")) : e("子包".concat(t.packageName, "大小").concat(parseInt(t.packageSize, 10), ", 下载耗时").concat(i, "ms"))) : "navigation" === t.entryType ? "appLaunch" === t.name ? ((0, jt.b)("appLaunch", {
                  du: i,
                  st: t.startTime,
                  path: l
                }), e("小程序启动耗时".concat(i, "ms"))) : "route" === t.name && (d = i, e("页面".concat(t.path, "路由耗时").concat(i, "ms"))) : "render" === t.entryType && ("firstPaint" === t.name ? (n = t.startTime, e("页面".concat(t.path, "首次绘制开始时间").concat(n, "ms, 耗时").concat(i, "ms"))) : "firstContentfulPaint" === t.name ? (o = t.startTime, r = o - n, e("页面".concat(t.path, "首次内容绘制开始时间").concat(o, "ms, 耗时").concat(i, "ms"))) : "largestContentfulPaint" === t.name && (s = t.startTime, a = s - o, e("页面".concat(t.path, "最大内容绘制开始时间").concat(s, "ms"))))
              }), e("".concat(l, " LCP duration: ").concat(a, "ms")), "appLaunch" !== c && (0, jt.b)("enterPage", {
                path: l,
                name: c,
                route: d,
                fp: n,
                fcp: o,
                fcpd: r,
                lcp: s,
                lcpd: a,
                pname: u,
                psize: p,
                pdl: h
              }), "function" == typeof se.a.getExtConfigSync && [12444, 11185, 205387].includes(Number(null == (g = se.a.getExtConfigSync()) ? void 0 : g.storeId))) {
              i(33).a.reportInfo("performance", f)
            }
          }).observe({
            entryTypes: ["render", "navigation", "loadPackage"]
          })
        }
      }
      se.a.getExtConfigSync = function (e) {
        return function () {
          return e()
        }
      }(se.a.getExtConfigSync);
      var Ft = i(34),
        Lt = i(35),
        Gt = i(38),
        Bt = i(36),
        Ht = i(37);
      (0, ae.z)((0, Bt.a)(Ht.a).app);
      var Wt = i(39),
        Vt = i(85),
        zt = i(33);
      const Kt = e => void Vt.g.commit("setAliNFCTagId", "");
      let Qt = null;
      if ((0, Wt.hb)()) try {
        const e = i(186).a;
        e.init(), Qt = e.gio
      } catch (e) {
        console.error(e)
      }
      var Jt = Qt;
      se.a.showModal = function (e) {
        return function (t) {
          return t.confirmText || (t.confirmText = se.a.i18n.t("global.confirm")), t.cancelText || (t.cancelText = se.a.i18n.t("global.cancel")), e(t)
        }
      }(se.a.showModal), se.a.getWindowInfo = function (e) {
        return function () {
          var t;
          if (!e) return function () {
            const e = se.a.getSystemInfoSync();
            return {
              pixelRatio: e.pixelRatio,
              safeArea: e.safeArea,
              screenHeight: e.screenHeight,
              screenTop: 0,
              screenWidth: e.screenWidth,
              statusBarHeight: e.statusBarHeight,
              windowHeight: e.windowHeight,
              windowWidth: e.windowWidth
            }
          }();
          return (null == (t = e()) ? void 0 : t.__returned) || e()
        }
      }(se.a.getWindowInfo);
      var $t = Object.defineProperty,
        Yt = Object.defineProperties,
        Zt = Object.getOwnPropertyDescriptors,
        Xt = Object.getOwnPropertySymbols,
        ei = Object.prototype.hasOwnProperty,
        ti = Object.prototype.propertyIsEnumerable,
        ii = (e, t, i) => t in e ? $t(e, t, {
          enumerable: !0,
          configurable: !0,
          writable: !0,
          value: i
        }) : e[t] = i;
      let ni = null;
      se.a.getMenuButtonBoundingClientRect = function (e) {
        return function () {
          const t = e() || {};
          return ni && !ni.top || (ni = t), i = ((e, t) => {
            for (var i in t || (t = {})) ei.call(t, i) && ii(e, i, t[i]);
            if (Xt)
              for (var i of Xt(t)) ti.call(t, i) && ii(e, i, t[i]);
            return e
          })({}, t), n = {
            bottom: t.bottom || ni.bottom || 83,
            height: t.height || ni.height || 32,
            left: t.left || ni.left || 296,
            right: t.right || ni.right || 383,
            top: t.top || ni.top || 51,
            width: t.width || ni.width || 87
          }, Yt(i, Zt(n));
          var i, n
        }
      }(se.a.getMenuButtonBoundingClientRect), Promise.prototype.finally || (Promise.prototype.finally = function (e) {
        const t = this.constructor;
        return this.then(i => t.resolve(e()).then(() => i), i => t.resolve(e()).then(() => {
          throw i
        }))
      }), Object.values || (Object.values = function (e) {
        if (e !== Object(e)) throw new TypeError("Object.values called on a non-object");
        return Object.keys(e).map(t => e[t])
      }), Array.prototype.includes || Object.defineProperty(Array.prototype, "includes", {
        value(e, t) {
          if (null == this) throw new TypeError('"this" is null or not defined');
          const i = Object(this),
            n = i.length >>> 0;
          if (0 === n) return !1;
          const o = 0 | t;
          let r = Math.max(o >= 0 ? o : n - Math.abs(o), 0);

          function s(e, t) {
            return e === t || "number" == typeof e && "number" == typeof t && isNaN(e) && isNaN(t)
          }
          for (; r < n;) {
            if (s(i[r], e)) return !0;
            r++
          }
          return !1
        }
      }), Promise.allSettled || (Promise.allSettled = function (e) {
        return new Promise((t, i) => {
          if (!Array.isArray(e)) return i(new TypeError("arguments must be an array"));
          var n = [],
            o = 0;
          0 === e.length ? t(n) : e.forEach((i, r) => {
            Promise.resolve(i).then(e => {
              n[r] = {
                status: "fulfilled",
                value: e
              }
            }, e => {
              n[r] = {
                status: "rejected",
                reason: e
              }
            }).finally(() => {
              ++o === e.length && t(n)
            })
          })
        })
      });
      var oi = i(129),
        ri = i(125),
        si = i(178),
        ai = i(124);
      let ci;
      try {
        (0, Wt.Pb)() && (ci = (0, Wt.ib)() ? i(187) : i(188), ci.init({
          token: {
            48875: "bica84f84f6e64461e",
            203683: "bid88af5abe8e343d0",
            201424: "bi3ec46521a1674234",
            206198: "bi94206658ccc841f5",
            27088: "bib104ac20361e4ce3",
            214925: "bid02b2fd81b4e48ff",
            203009: "biae260d5a9ec946a2",
            216627: "bic2796fdb27b548f1"
          } [(0, ai.g)().storeId] || "",
          appid: (0, ai.g)().appid,
          usePlugin: !1,
          debug: !0,
          autoProxy: {
            app_launch: !0,
            app_show: !0,
            app_exit: !0,
            browse_page: !1,
            leave_page: !1,
            autoTrack: !0,
            page_pull_down_refresh: !0,
            page_reach_bottom: !0,
            page_share_app_message: !1,
            openAutoTrackOpenId: !1,
            openAutoTrackUnionId: !1
          }
        }))
      } catch (D) {
        console.error("youshu init error", D)
      }
      var li = ci,
        ui = i(189),
        hi = i(134),
        pi = i(127),
        di = i(148),
        gi = i(151);
      const fi = App;
      App = function (e) {
        const t = e.onShow;
        return e.onShow = function (e) {
          ri.l.commit("setScene", e.scene), t && t.call(this, e)
        }, fi && fi(e)
      };
      const mi = Page;
      Page = function (e) {
        const t = e.onLoad;
        e.onLoad = function (e) {
          const i = getApp();
          if (i.globalData.switchParams && (e = Object.assign(e, i.globalData.switchParams), i.globalData.switchParams = null), e.channelCode && ri.l.commit("setChannelCode", e.channelCode), e.q) {
            const t = decodeURIComponent(e.q);
            ri.l.commit("setQrCode", t), ri.l.commit("setPromotionCode", t);
            const i = (0, si.h)(t);
            i && i.length < 16 && ri.l.commit("setChannelCode", i)
          }
          if (ri.l.state.activityScene) {
            if (e.scene) {
              const t = decodeURIComponent(e.scene).slice(2);
              e.activityId = t, e.scene = null, ri.l.dispatch("activitySceneParams", e)
            }
            ri.l.commit("setActivityScene", "")
          }
          if (e.inviteUserId && e.inviteActivityId && e.inviteActivityType && ri.l.commit("setInviteTaskData", {
              inviteUserId: e.inviteUserId,
              activityId: e.inviteActivityId,
              type: e.inviteActivityType
            }), e.gdt_vid && (ri.l.commit("setGdtVid", e.gdt_vid), Vt.g.commit("setGdtVid", e.gdt_vid)), e.qz_gtd && (ri.l.commit("setQzGtd", e.qz_gtd), Vt.g.commit("setQzGtd", e.qz_gtd)), !ri.l.state.isReady && !ui.a.includes(this.route)) return t && (0, di.b)({
            fn: t.bind(this, e),
            route: this.route
          });
          return t && t.call(this, e)
        };
        const i = e.onShow;
        e.onShow = function () {
          const e = {};
          if ("function" == typeof this.getTabBar && this.getTabBar() && (this.getTabBar().$forceUpdate({
              path: this.route
            }), (0, oi.d)(this.route) && "pages/takefood/index" == this.route && !ri.l.state.nav)) {
            if (!ri.l.state.isReady && !ui.a.includes(this.route)) return i && (0, di.b)({
              fn: i.bind(this, e),
              route: this.route
            });
            return i && i.call(this, e)
          }
          if ((0, Wt.Pb)() && li.track("browse_wxapp_page", {
              page: (0, gi.a)(),
              page_title: (0, gi.c)() || "未知",
              refer_page: (0, gi.a)(1),
              is_sdk_auto_track: !0
            }), !ri.l.state.isReady && !ui.a.includes(this.route)) return i && (0, di.b)({
            fn: i.bind(this, e),
            route: this.route
          });
          return i && i.call(this, e)
        };
        const n = e.onReady;
        e.onReady = function () {
          if (!ri.l.state.isReady && !ui.a.includes(this.route)) return n && (0, di.b)({
            fn: n.bind(this),
            route: this.route
          });
          return n && n.call(this)
        };
        const o = e.onHide;
        e.onHide = function () {
          return (0, Wt.Pb)() && li.track("leave_wxapp_page", {
            page: (0, gi.a)(),
            page_title: (0, gi.c)() || "未知",
            refer_page: (0, gi.a)(1),
            stay_time: e.__enterTime__ ? Date.now() - e.__enterTime__ : 0,
            is_sdk_auto_track: !0
          }), o && o.call(this)
        };
        const r = e.onUnload;
        e.onUnload = function () {
          return (0, Wt.Pb)() && li.track("leave_wxapp_page", {
            page: (0, gi.a)(),
            page_title: (0, gi.c)() || "未知",
            refer_page: (0, gi.a)(1),
            stay_time: e.__enterTime__ ? Date.now() - e.__enterTime__ : 0,
            is_sdk_auto_track: !0
          }), r && r.call(this)
        };
        const s = e.onShareAppMessage;
        return s && (e.onShareAppMessage = function (e) {
          const t = s && s.call(this, e);
          if ((0, Wt.Pb)() && t) {
            if ((0, hi.c)(t)) return new Promise(i => {
              t.then(t => {
                try {
                  li.track("page_share_app_message", {
                    from_type: e.from,
                    share_title: t.title || "分享",
                    share_path: t.path,
                    share_image_url: t.bgImgUrl || t.imageUrl
                  })
                } catch (e) {
                  console.error(e)
                }
                i(t)
              })
            });
            try {
              li.track("page_share_app_message", {
                from_type: e.from,
                share_title: t.title || "分享",
                share_path: t.path,
                share_image_url: t.bgImgUrl || t.imageUrl
              })
            } catch (e) {
              console.error(e)
            }
          }
          return t
        }), mi(e)
      };
      var yi = i(122),
        vi = i(190),
        _i = i(132);
      let bi = "";
      bi = "wx";
      const ki = {
        platform: bi,
        qmFromType: "catering",
        pageType: {
          "pages/index/index": "indexPage",
          "pages/takefood/index": "goodsList",
          "subpackages/confirm/confirm": "orderConfirm",
          "pages/order/list/list": "orderCenter",
          "subpackages/detail/index": "orderFinish",
          "pages/user/index": "userCenter",
          "pages/pay/index/index": "payBill"
        },
        scene() {
          return ri.l.state.scene || ""
        },
        sid() {
          var e;
          return (null == (e = (0, ai.g)()) ? void 0 : e.storeId) || 0
        },
        mid() {
          var e;
          return (null == (e = ri.k.state.current) ? void 0 : e.id) || 0
        },
        mname() {
          var e;
          return (null == (e = ri.k.state.current) ? void 0 : e.name) || ""
        },
        saleType() {
          return 1 == ri.l.state.saleType ? 3 : 1
        },
        uid() {
          return ri.n.getters.getUserInfoByKey("id") || ""
        },
        uuid() {
          return ri.n.getters.getUserInfoByKey("unionid") || ""
        },
        openid() {
          return ri.n.getters.getUserInfoByKey("openid") || ""
        },
        lng() {
          const e = (0, _i.a)("location");
          return e ? (0, yi.encryptApiParams)(e.longitude) : ""
        },
        lat() {
          const e = (0, _i.a)("location");
          return e ? (0, yi.encryptApiParams)(e.latitude) : ""
        },
        code() {
          return ri.l.state.channelCode || ""
        },
        qrCode() {
          return ri.l.state.qrCode || ""
        },
        proCode() {
          return ri.l.state.promotionCode || ""
        },
        mobile() {
          return ri.n.state.mobile ? (0, pi.a)(ri.n.state.mobile) : ""
        },
        theme() {
          return ri.f.state.theme || ""
        },
        locale() {
          return ri.l.state.locale
        },
        tabBarPageOffsetTopMap() {
          return ri.b.state.tabBarPageOffsetTopMap
        },
        globalPageTitle() {
          return ri.l.state.globalPageTitle
        },
        disableReport() {
          return ri.b.state.appConfig.disableReport
        },
        debug: !0
      };
      vi.b.init(ki);
      var Si = i(156),
        xi = Object.defineProperty,
        wi = Object.defineProperties,
        Ti = Object.getOwnPropertyDescriptors,
        Ii = Object.getOwnPropertySymbols,
        Ci = Object.prototype.hasOwnProperty,
        Oi = Object.prototype.propertyIsEnumerable,
        Pi = (e, t, i) => t in e ? xi(e, t, {
          enumerable: !0,
          configurable: !0,
          writable: !0,
          value: i
        }) : e[t] = i;
      zt.a.registerApp({
        getAppTrace() {
          return (0, vi.a)()
        },
        userInfo() {
          const e = ri.n.state;
          return t = ((e, t) => {
            for (var i in t || (t = {})) Ci.call(t, i) && Pi(e, i, t[i]);
            if (Ii)
              for (var i of Ii(t)) Oi.call(t, i) && Pi(e, i, t[i]);
            return e
          })({}, e), i = {
            mobile: (0, pi.a)(e.mobile)
          }, wi(t, Ti(i));
          var t, i
        },
        disableReport() {
          return ri.b.state.appConfig.disableReport || !1
        },
        shopInfo() {
          return {
            id: ri.k.getters.shopId || "",
            name: ri.k.getters.shopName || ""
          }
        },
        userToken() {
          return (0, Si.a)()
        },
        networkInfo() {
          return ri.l.state.networkStatus
        }
      });
      var Ai = i(157); {
        const e = i(158),
          t = (0, ai.g)().storeId,
          n = {
            10964: "https://tracking.yonghe.com.cn/sa?project=default",
            42742: "https://tracking.yonghe.com.cn/sa?project=default",
            203683: "https://tracking.yonghe.com.cn/sa?project=default",
            49006: "https://upload-tracking-cn.chagee.com/sa?project=chn_dev",
            207720: "https://upload-tracking-cn.chagee.com/sa?project=chn_dev",
            205387: "https://upload-tracking-cn.chagee.com/sa?project=chn_dev",
            11322: "https://upload-tracking-cn.chagee.com/sa?project=chn_dev"
          },
          o = {
            42742: "JFCC",
            203683: "JFCC"
          },
          r = {
            42742: "外送到家",
            203683: "堂食点餐"
          },
          s = {
            42742: "YHK",
            203683: "YHK"
          };
        ((0, Wt.Ob)() || (0, Wt.Nb)()) && (e.setPara({
          name: "sensors",
          server_url: n[t] || "",
          autoTrack: {
            mpClick: !0
          },
          source_channel: [],
          show_log: !0,
          allow_amend_share_path: !1
        }), e.registerApp({
          is_login: !!e.store.getFirstId(),
          app_name: r[t],
          merchant_id: o[t],
          brand_id: s[t]
        }))
      }
      if ((0, Wt.Z)()) {
        const {
          sensors: e
        } = (0, Ai.j)(), t = (0, ai.g)().storeId, i = {
          49006: "https://upload-tracking-cn.chagee.com/sa?project=chn_production",
          207720: "https://upload-tracking-cn.chagee.com/sa?project=chn_production",
          11322: "https://upload-tracking-cn.chagee.com/sa?project=chn_dev"
        };
        (0, Ai.g)(), e.setPara({
          name: "sensors",
          server_url: i[t] || "",
          autoTrack: {
            mpClick: !0,
            pageLeave: !0
          },
          source_channel: [],
          show_log: !0,
          allow_amend_share_path: !1
        }), e.registerApp({
          pub_platform_name: "霸王茶姬".concat(ai.m, "小程序"),
          pub_platform_version: (0, ai.g)().appVersion,
          pub_is_login() {
            return !!ri.n.state.mobile
          },
          pub_is_member() {
            return !!ri.n.state.mobile
          },
          pub_vip_level() {
            return ri.n.state.memberLevel || ""
          },
          pub_country: "中国",
          pub_province() {
            return (ri.l.state.userAddress || {
              province: ""
            }).province || ""
          },
          pub_city() {
            const e = ri.l.state.userAddress || {
              city: "",
              district: ""
            };
            return e.city || e.district
          },
          utm_channel_code() {
            return ri.l.state.channelCode
          }
        })
      }
      var Ei = i(183),
        Ri = i(191),
        Ni = i.n(Ri),
        Di = i(143);
      var qi = i(135),
        Mi = i(155);
      var Ui = i(130),
        ji = i(121),
        Fi = Object.defineProperty,
        Li = Object.defineProperties,
        Gi = Object.getOwnPropertyDescriptors,
        Bi = Object.getOwnPropertySymbols,
        Hi = Object.prototype.hasOwnProperty,
        Wi = Object.prototype.propertyIsEnumerable,
        Vi = (e, t, i) => t in e ? Fi(e, t, {
          enumerable: !0,
          configurable: !0,
          writable: !0,
          value: i
        }) : e[t] = i,
        zi = (e, t) => {
          for (var i in t || (t = {})) Hi.call(t, i) && Vi(e, i, t[i]);
          if (Bi)
            for (var i of Bi(t)) Wi.call(t, i) && Vi(e, i, t[i]);
          return e
        },
        Ki = (e, t) => Li(e, Gi(t));
      const Qi = function () {
          let e, t, i;
          const n = Array.prototype.shift,
            o = Array.prototype.unshift,
            r = {};
          let s;
          const a = {},
            c = function (e, t) {
              let i;
              for (let n = 0, o = e.length; n < o; n++) {
                const o = e[n];
                i = t.call(o, n, o)
              }
              return i
            };
          return e = function (e, t, i) {
            i[e] || (i[e] = []), i[e].push(t)
          }, i = function (e, t, i) {
            if (t[e])
              if (i)
                for (let n = t[e].length; n >= 0; n--) t[e][n] === i && t[e].splice(n, 1);
              else t[e] = []
          }, t = function () {
            const e = n.call(arguments),
              t = n.call(arguments),
              i = arguments,
              o = this,
              r = e[t];
            if (!r || !r.length) return;
            return c(r, function () {
              return this.apply(o, i)
            })
          }, s = function (n) {
            n = n || "default";
            const s = {},
              l = {
                listen(t, i, n) {
                  if (e(t, i, s), null === a[t]) return;
                  "last" === n ? a[t] && a[t].length && a[t].pop()() : c(a[t] || [], function () {
                    this()
                  }), a[t] = null
                },
                one(e, t, n) {
                  i(e, s), this.listen(e, t, n)
                },
                remove(e, t) {
                  i(e, s, t)
                },
                trigger(e) {
                  let i, n;
                  const r = this;
                  return o.call(arguments, s), n = arguments, i = function () {
                    return t.apply(r, n)
                  }, a[e] = [], a[e].push(i), i()
                }
              };
            return n ? r[n] ? r[n] : r[n] = l : l
          }, {
            create: s,
            one(e, t, i) {
              this.create().one(e, t, i)
            },
            remove(e, t) {
              this.create().remove(e, t)
            },
            listen(e, t, i) {
              this.create().listen(e, t, i)
            },
            trigger() {
              this.create().trigger.apply(this, arguments)
            }
          }
        }(),
        Ji = (0, qi.a)(),
        $i = (0, ai.g)();
      ! function (e, t = {}) {
        const n = [{
          getMpx() {
            return se.a
          }
        }];
        n.push({
          onLaunch() {
            Object.assign(this, se.a.prototype)
          }
        }), i.g.qmaiOpenExtendTasks && (i.g.qmaiOpenExtendTasks.forEach(t => {
          for (const i in t)
            if ("object" == typeof t[i]) e[i] = Object.assign({}, e[i] || null, t[i]);
            else if ("function" == typeof t[i]) {
            const n = e[i] || function () {};
            e[i] = function (...e) {
              try {
                t[i].apply(this, e)
              } catch (e) {
                console.error("[qmai-open runtime error] Error in custom ".concat(i, " function:"), e)
              }
              return n.apply(this, e)
            }
          }
        }), i.g.qmaiOpenExtendTasks = null);
        const {
          rawOptions: o,
          currentInject: r
        } = (0, Ft.a)(e, "app", !1);
        o.mixins = n;
        const s = function (e) {
          const t = {};
          return Object.keys(e).forEach(i => {
            if (Gt.a[i]) return;
            t[i] = e[i]
          }), t
        }((0, ae.H)((0, Lt.a)(o, "app", !1), "methods"));
        s.onAppInit && s.onAppInit(), (t.customCtor || i.g.currentCtor || App)(s)
      }({
        eventEmitter: new(Ni()),
        $on: Qi.listen.bind(Qi),
        $once: Qi.one.bind(Qi),
        $off: Qi.remove.bind(Qi),
        $emit: Qi.trigger.bind(Qi),
        handleTokenExpired: !1,
        globalData: {
          colorThemeLight: $i.colorTheme ? "".concat($i.colorTheme, "1d") : "",
          imgPathPre: "https://images.qmai.cn",
          query: {},
          popRecordLog: {},
          adverRecordLog: {},
          isWebp: (0, si.n)(),
          firstBannerCurrent: 0,
          bgList: [],
          switchParams: null,
          crypto: {
            getRandomValues: se.a.getRandomValues
          }
        },
        umengConfig: {
          appKey: {
            wx57da7f4b6d0763b2: "5f648634a4ae0a7f7d08a0a7",
            wxf82c67261b8f6a8b: "5f64867ba4ae0a7f7d08a35e",
            wxd92a2d29f8022f40: "60dc33368a102159db82ff7b",
            wx5dbb2acbfb559d9e: "60dd2f5b26a57f101841a14a"
          } [$i.appid] || "placeholder",
          useOpenid: !1,
          autoGetOpenid: !1,
          debug: !1,
          uploadUserInfo: !0
        },
        sr: li,
        gio: Jt,
        onLaunch(e) {
          return __async(this, null, function* () {
            this._handleOptions(e), se.a.onLazyLoadError(e => {
              zt.a.reportError("onLazyLoadError", e)
            }), this.$on("loginSuccess", () => {
              (0, Di.b)({
                init: !0
              }), console.log(e, "app options"), (0, Wt.e)(e), (0, Mi.a)()
            }), this.$once("tokenExpired", () => __async(this, null, function* () {
              if (this.handleTokenExpired) return;
              this.handleTokenExpired = !0, yield(0, ji.fetchLogin)({
                scene: "init",
                forceLogin: !0
              }).catch(() => {
                (0, _i.c)("loginData")
              }).finally(() => {
                this.handleTokenExpired = !1
              }), (0, oi.h)({
                path: e.path,
                query: e.query,
                reason: "tokenExpired"
              })
            })), this.$on("getCommonInfo", () => __async(this, null, function* () {
              const e = "true" == ri.l.state.configCenterByKeys["Design.internationalization"];
              yield ri.l.dispatch("loadLocale", e ? void 0 : ri.l.state.defaultLanguage), (0, di.a)()
            }));
            const t = (0, ai.g)();
            ri.l.commit("setExtConfig", t), Vt.g.commit("setPrimaryColor", t.colorTheme || ""), ri.l.commit("setSystemInfo", Ji), ri.l.dispatch("getGlobalPageTitle"), (0, pi.f)()
          })
        },
        onShow(e) {
          return __async(this, null, function* () {
            const t = (0, Wt.D)();
            zt.a.reportInfo("启动参数", {
              options: e,
              enterOptions: t
            }), Vt.g.commit("setEnterOptions", t), ri.l.dispatch("activitySceneOnshow", e), Kt(), this.handleNetworkChange(), this.handleRedirect(e), Wt.N.handleStatus(e), yield ri.b.dispatch("getAppConfig"), ri.l.dispatch("getWxPlugins"), (0, Di.c)(), ui.b.includes(e.path) || e.query && e.query.sellerId || (0, ji.fetchLogin)({
              scene: "init",
              source: "appOnShow"
            })
          })
        },
        _handleOptions(e) {
          const t = e.query || {};
          t.workWechatUserid && ri.l.commit("setWorkWechatUserid", t.workWechatUserid); {
            let e = "";
            if (e = t.q, e) {
              const t = decodeURIComponent(e);
              ri.l.commit("setPromotionCode", t);
              const i = (0, si.h)(t);
              i && i.length < 16 && (ri.l.commit("setChannelCode", i), ri.l.commit("setQrCode", t), (0, Ai.f)(i))
            } else t.channelCode && (ri.l.commit("setChannelCode", t.channelCode), (0, Ai.f)(t.channelCode))
          }
          t.multi_id && ri.l.dispatch("switchShop", t.multi_id)
        },
        handleNetworkChange() {
          se.a.onNetworkWeakChange && se.a.onNetworkWeakChange(e => {
            ri.l.commit("setNetworkStatus", Ki(zi({}, ri.l.state.networkStatus), {
              weak: e.weakNet ? 1 : 0
            }))
          }), se.a.onNetworkStatusChange && se.a.onNetworkStatusChange(e => {
            e.isConnected || se.a.showToast({
              title: "网络异常，请检查您的网络设置"
            }), ri.l.commit("setNetworkStatus", Ki(zi({}, ri.l.state.networkStatus), {
              connected: e.isConnected ? 1 : 0,
              type: e.networkType
            }))
          })
        },
        onPageNotFound(e) {
          const {
            path: t,
            query: i
          } = e || {};
          if ("pages/home/home" === t)(0, oi.h)({
            query: i,
            reason: "pages/home/home"
          });
          else if ("subpackages/detail/invoicing-detail/index" === t) {
            i && i.q && (i.oldPage = "invoicingDetail");
            const e = (0, Wt.cc)("/subpackages/detail/index", i);
            (0, oi.i)(e)
          } else if (Ui.k["/".concat(t)]) {
            const e = (0, Wt.cc)("/".concat(t), i);
            (0, oi.i)(e)
          } else zt.a.reportError("onPageNotFound", e), (0, oi.h)({
            query: i,
            reason: "onPageNotFound"
          })
        },
        onError(e, t) {
          zt.a.onError(e, t)
        },
        onUnhandledRejection(e) {
          zt.a.onUnhandledRejection(e)
        },
        handleRedirect(e) {
          const {
            path: t,
            query: i
          } = e || {};
          if ("subpackages/tabbar-pages/index/index" === e.path && (0, oi.h)({
              query: i,
              reason: "首页重定向"
            }), Ui.k["/".concat(t)]) {
            const e = (0, Wt.cc)("/".concat(t), i);
            (0, oi.i)(e)
          }
        },
        onHide() {
          se.a.offNetworkStatusChange && se.a.offNetworkStatusChange(), se.a.offNetworkWeakChange && se.a.offNetworkWeakChange()
        },
        openApiAuthLogin(e) {
          return __async(this, null, function* () {
            0
          })
        },
        openApiBindMobile(e) {
          return __async(this, null, function* () {
            0
          })
        },
        tracker: Ei.d
      }, {
        customCtor: App
      })
    },
    186: function (e, t, i) {
      "use strict";
      i.d(t, {
        a: function () {
          return Ne
        }
      });
      const n = e => ["undefined", "null"].includes(O(e)),
        o = e => "string" === O(e),
        r = e => "number" === O(e),
        s = e => "boolean" === O(e),
        a = e => "[object Object]" === {}.toString.call(e) && !n(e),
        c = e => ["function", "asyncfunction"].includes(O(e)),
        l = e => Array.isArray(e) && "array" === O(e),
        u = e => {
          try {
            return Array.from(e)[0]
          } catch (e) {
            return
          }
        },
        h = e => {
          try {
            const t = Array.from(e);
            return t[t.length - 1]
          } catch (e) {
            return
          }
        },
        p = (e, t = 1) => l(e) && r(t) ? e.slice(t > 0 ? t : 1, e.length) : e,
        d = e => {
          if (l(e)) {
            let t = 0;
            const i = [];
            for (const n of e) n && !C(n) && (i[t++] = n);
            return i
          }
          return e
        },
        g = (e, t) => {
          if (l(e)) {
            const i = e.findIndex(t);
            return 0 > i ? void 0 : e[i]
          }
        },
        f = e => n(e) ? "" : "" + e,
        m = (e, t) => "string" === O(e) ? e.split(t) : e,
        y = e => {
          if (o(e)) {
            const t = m(e, "");
            return "".concat(u(t).toLowerCase()).concat(p(t).join(""))
          }
          return e
        },
        v = (e, t) => e.slice(0, t.length) === t,
        _ = {}.hasOwnProperty,
        b = (e, t) => !n(e) && _.call(e, t),
        k = e => a(e) ? Object.keys(e) : [],
        S = (e, t) => {
          k(e).forEach(i => t(e[i], i))
        },
        x = (e, t) => {
          const i = k(e);
          return !(!a(e) || !a(t) || i.length !== k(t).length || i.map((i, n) => a(e[i]) ? x(e[i], t[i]) : e[i] === t[i]).includes(!1))
        },
        w = (e, t, i) => {
          let n = e;
          return a(e) ? (t.split(".").forEach(e => {
            n = n ? n[e] : i
          }), n) : i
        },
        T = (e, t) => {
          if (!a(e)) return !1;
          try {
            if ("string" === O(t)) return delete e[t];
            if ("array" === O(t)) return t.map(t => delete e[t]);
            "object" === O(t) && t.constructor === RegExp && k(e).forEach(i => {
              t.test(i) && T(e, i)
            })
          } catch (e) {
            return !1
          }
        },
        I = (e, t = 250, i, n) => {
          let o, r = 0;
          return "boolean" !== O(i) && (n = e, e = i, i = void 0),
            function (...s) {
              let a = this,
                c = Date.now() - r;

              function l() {
                r = Date.now(), e.apply(a, s)
              }
              n && !o && l(), o && clearTimeout(o), void 0 === n && c > t ? l() : !0 !== i && (o = setTimeout(n ? function () {
                o = void 0
              } : l, void 0 === n ? t - c : t))
            }
        },
        C = e => l(e) ? 0 === e.length : a(e) ? 0 === k(e).length : !e,
        O = e => ({}.toString.call(e).slice(8, -1).toLowerCase());
      var P = Object.freeze({
        __proto__: null,
        isNil: n,
        isString: o,
        isNaN: e => "NaN" === f(Number(e)),
        isNumber: r,
        isBoolean: s,
        isObject: a,
        isRegExp: e => "[object RegExp]" === {}.toString.call(e),
        isFunction: c,
        isArray: l,
        isDate: e => "date" === O(e),
        fixed: (e, t) => r(e) ? Number(e.toFixed(r(t) ? t : 2)) : o(e) && "NaN" !== f(Number(e)) ? Number(Number(e).toFixed(r(t) ? t : 2)) : e,
        head: u,
        last: h,
        drop: p,
        dropWhile: (e, t) => l(e) ? e.filter(e => !t(e)) : e,
        compact: d,
        find: g,
        isEqualArray: (e, t) => !(!l(e) || !l(t) || e.length !== t.length) && e.every((e, i) => e === t[i]),
        toString: f,
        split: m,
        lowerFirst: y,
        upperFirst: e => {
          if (o(e)) {
            const t = m(e, "");
            return "".concat(u(t).toUpperCase()).concat(p(t).join(""))
          }
          return e
        },
        startsWith: v,
        endsWith: (e, t) => {
          const {
            length: i
          } = e;
          let n = i;
          n > i && (n = i);
          const o = n;
          return n -= t.length, n >= 0 && e.slice(n, o) === t
        },
        hasOwnProperty: _,
        has: b,
        keys: k,
        forEach: S,
        isEqual: x,
        get: w,
        unset: T,
        throttle: I,
        isEmpty: C,
        typeOf: O,
        formatDate: e => {
          function t(e) {
            return 10 > e ? "0" + e : e
          }
          return e.getFullYear() + "-" + t(e.getMonth() + 1) + "-" + t(e.getDate()) + " " + t(e.getHours()) + ":" + t(e.getMinutes()) + ":" + t(e.getSeconds()) + "." + t(e.getMilliseconds())
        }
      });
      const A = (e, t) => {
          console.log("%c[GrowingIO]：" + e, {
            info: "color: #3B82F6;",
            error: "color: #EF4444",
            warn: "color: #F59E0B",
            success: "color: #10B981"
          } [t] || "")
        },
        E = (e, t = !0, i = "参数不合法") => A("".concat(t ? "调用" : "设置", " ").concat(e, " 失败，").concat(i, "!"), "warn"),
        R = e => {
          try {
            return e()
          } catch (e) {
            return
          }
        },
        N = e => o(e) ? e.trim().substring(0, 100) : e,
        D = (e, t) => o(e) && !C(e) && e.match(/^[a-zA-Z_][0-9a-zA-Z_]{0,100}$/) ? t() : (A("事件名格式不正确，只能包含数字、字母和下划线，且不能以数字开头，字符总长度不能超过100!", "error"), !1),
        q = () => "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (e) {
          const t = 16 * Math.random() | 0;
          return ("x" === e ? t : 3 & t | 8).toString(16)
        }),
        M = e => e.pixelRatio ? Math.round(e.screenHeight * e.pixelRatio) : e.screenHeight,
        U = e => e.pixelRatio ? Math.round(e.screenWidth * e.pixelRatio) : e.screenWidth,
        j = (e, t) => {
          if (e) {
            const i = e.toLowerCase();
            return -1 !== i.indexOf("android") ? t + "-Android" : -1 !== i.indexOf("ios") ? t + "-iOS" : e
          }
        },
        F = e => {
          if (o(e)) {
            const t = e.indexOf("?");
            return -1 !== t ? [e.substring(0, t), e.substring(t + 1)] : [e, ""]
          }
          return ["", ""]
        },
        L = e => o(e) ? e.startsWith("/") ? e : "/" + e : "",
        G = e => R(() => {
          switch (e) {
            case "wx":
              return wx;
            case "my":
            case "tb":
              return my;
            case "swan":
              return swan;
            case "tt":
              return tt;
            case "qq":
              return qq;
            case "ks":
              return ks;
            case "jd":
              return jd;
            default: {
              let e;
              return e || (e = R(() => swan)), e || (e = R(() => my)), e || (e = R(() => tt)), e || (e = R(() => qq)), e || (e = R(() => ks)), e || (e = R(() => jd)), e || (e = R(() => wx)), e
            }
          }
        }),
        B = e => R(() => {
          switch (e) {
            case "wx":
              return __wxConfig;
            case "swan":
              return appConfig;
            case "tt":
              return __ttConfig;
            case "qq":
              return __qqConfig;
            case "ks":
              return __ksConfig;
            case "jd":
              return __jdConfig;
            default:
              return
          }
        }),
        H = () => {
          let e;
          return !e && R(() => swan) && (e = "swan"), !e && R(() => tt) && (e = "tt"), !e && R(() => qq) && (e = "qq"), !e && R(() => my.tb) && (e = "tb"), !e && R(() => my) && (e = "my"), !e && R(() => ks) && (e = "ks"), !e && R(() => jd) && (e = "jd"), !e && R(() => wx) && (e = "wx"), e || g(k(i.g), e => f(e).toLowerCase().includes("quickapp")) && (e = "quickapp"), e
        },
        W = e => k(e).filter(e => e.indexOf("__sub") > -1 && e.indexOf("gio__") > -1).sort(),
        V = () => {
          let e = R(() => getApp({
            allowDefault: !0
          }));
          return e || (e = z()), e
        },
        z = () => {
          var e;
          return null !== (e = R(() => $global)) && void 0 !== e ? e : i.g
        },
        K = e => {
          const t = {};
          return a(e) && S(e, (e, i) => {
            const o = f(i).slice(0, 100);
            a(e) ? t[o] = K(e) : l(e) ? (t[o] = e.slice(0, 100), t[o] = t[o].join("||").slice(0, 1e3)) : t[o] = n(e) ? "" : f(e).slice(0, 1e3)
          }), t
        },
        Q = (e, t) => {
          const i = () => t.map(t => e.getStorageSync(t));
          try {
            return e.minip.canIUse("batchGetStorageSync") ? e.minip.batchGetStorageSync(t) : i()
          } catch (e) {
            return i()
          }
        },
        J = (e, t) => {
          const i = () => t.map(({
            key: t,
            value: i
          }) => e.setStorageSync(t, i));
          try {
            return e.minip.canIUse("batchSetStorageSync") ? e.minip.batchSetStorageSync(t) : i()
          } catch (e) {
            return i()
          }
        },
        $ = e => k(e || {}).map(t => t ? "".concat(t, "=").concat(n(e[t]) ? "" : e[t]) : "").join("&"),
        Y = e => {
          (v(e, "?") || v(e, "&")) && (e = e.slice(1, e.length));
          const t = {};
          return e.split("&").forEach(e => {
            const i = e.split("=");
            i[0] && (t[i[0]] = i[1])
          }), t
        };
      var Z = Object.freeze({
        __proto__: null,
        consoleText: A,
        callError: E,
        niceTry: R,
        niceCallback: (e, t) => {
          if (c(e)) try {
            e(t)
          } catch (e) {
            A("回调执行失败！" + e, "error")
          }
        },
        limitString: N,
        eventNameValidate: D,
        guid: q,
        getScreenHeight: M,
        getScreenWidth: U,
        getOS: j,
        compareVersion: (e = "", t = "") => {
          const i = e => e.replace(/\s+/g, ""),
            n = e => e.replace(/[vV]/g, ""),
            o = i(n(e)),
            r = i(n(t)),
            s = o.split("."),
            a = r.split(".");
          for (let e = 0; 3 > e; e++) {
            let t = Number(s[e]),
              i = Number(a[e]);
            if (t > i) return 1;
            if (i > t) return -1;
            if (!isNaN(t) && isNaN(i)) return 1;
            if (isNaN(t) && !isNaN(i)) return -1
          }
          return 0
        },
        getVueVersion: e => {
          if (e) {
            const t = Number.parseInt(u(m(e.version, ".")), 10);
            return Number.isNaN(t) ? 0 : t
          }
          return 0
        },
        splitPath: F,
        normalPath: L,
        isTaro3: e => {
          const {
            Current: t,
            createComponent: i
          } = e;
          return !(!e || !t || i)
        },
        getPlainMinip: G,
        getPlainConfig: B,
        getPlainPlatform: H,
        getSubKeys: W,
        getAppInst: V,
        getGlobal: z,
        limitObject: K,
        batchGetStorageSync: Q,
        batchSetStorageSync: J,
        qsStringify: $,
        qsParse: Y,
        hashCode: e => {
          let t = 0;
          if (C(e) || "boolean" == typeof e) return t;
          let i = 0;
          for (; i < e.length;) t = (t << 5) - t + e.charCodeAt(i), t &= t, i++;
          return t
        }
      });
      const X = e => o(e) && e.length > 0 || r(e) && e > 0,
        ee = {
          autotrack: {
            type: "boolean",
            default: !0
          },
          compress: {
            type: "boolean",
            default: !0
          },
          dataCollect: {
            type: "boolean",
            default: !0
          },
          debug: {
            type: "boolean",
            default: !1
          },
          idMapping: {
            type: "boolean",
            default: !1
          },
          enableIdMapping: {
            type: "boolean",
            default: !1
          },
          extraParams: {
            type: "array",
            default: []
          },
          followShare: {
            type: "boolean",
            default: !0
          },
          forceLogin: {
            type: "boolean",
            default: !1
          },
          ignoreFields: {
            type: "array",
            default: []
          },
          pluginMode: {
            type: "boolean",
            default: !1
          },
          originalSource: {
            type: "boolean",
            default: !0
          },
          keepAlive: {
            type: "number",
            default: 3e5
          },
          performance: {
            type: "object",
            default: {
              monitor: !0,
              exception: !0
            }
          },
          serverUrl: {
            type: "string",
            default: "https://napi.growingio.com"
          },
          subpackage: {
            type: "boolean",
            default: !1
          },
          taro: {
            type: ["object", "module"],
            default: !1
          },
          taroVue: {
            type: ["object", "function"],
            default: !1
          },
          tbConfig: {
            type: "object",
            default: {
              cloud: void 0,
              cloudFuncSend: !1,
              cloudFuncName: "httpTunnel",
              cloudFuncHandler: "main",
              cloudAppId: void 0,
              path: void 0
            }
          },
          uniVue: {
            type: ["object", "function"],
            default: !1
          },
          uploadInterval: {
            type: "number",
            default: 1e3
          },
          version: {
            type: "string",
            default: "1.0.0"
          }
        },
        te = ["clearGeneralProps", "clearTrackTimer", "clearUserId", "getDeviceId", "getGioInfo", "getOption", "identify", "init", "registerPlugins", "removeTimer", "setGeneralProps", "setLocation", "setOption", "setPageAttributes", "setUserAttributes", "setUserId", "track", "trackTimerEnd", "trackTimerPause", "trackTimerResume", "trackTimerStart", "updateImpression", "getABTest"],
        ie = {
          autotrack: "无埋点",
          dataCollect: "数据采集",
          debug: "调试模式",
          serverUrl: "数据上报服务地址"
        },
        ne = ["enableDebug", "setAutotrack", "setDataCollect", "setTrackerHost", "setTrackerScheme", "setConfig", "collectImp", "setPlatformProfile", "getLocation"],
        oe = ["deviceBrand", "deviceModel", "deviceType", "networkState", "screenHeight", "screenWidth", "operatingSystem"],
        re = [...oe, "appChannel", "language", "platformVersion"];
      class se {
        constructor(e) {
          this.growingIO = e, this.main = e => {
            var t, i, n, o, r;
            const {
              sdkVersion: s,
              vdsConfig: a,
              platformConfig: c,
              minipInstance: l,
              userStore: u,
              dataStore: {
                scene: h,
                eventHooks: p,
                locationData: d,
                lastVisitEvent: g
              }
            } = this.growingIO, {
              systemInfo: f = {},
              network: m = {}
            } = l, {
              brand: y,
              model: v,
              platform: _,
              language: b,
              version: k
            } = f, S = {
              appChannel: "scn:" + (h || "NA"),
              appVersion: a.version,
              dataSourceId: a.dataSourceId,
              deviceBrand: y,
              deviceId: u.uid,
              deviceModel: v,
              deviceType: j(_, c.name),
              domain: a.appId,
              language: b,
              latitude: null == d ? void 0 : d.latitude,
              longitude: null == d ? void 0 : d.longitude,
              networkState: (null == m ? void 0 : m.networkType) || (null == m ? void 0 : m.type) || (null == m ? void 0 : m.subtype),
              operatingSystem: j(_, c.name),
              path: (null === (t = p.currentPage) || void 0 === t ? void 0 : t.path) ? null === (i = p.currentPage) || void 0 === i ? void 0 : i.path : g.path,
              platform: c.platform,
              platformVersion: c.name + (k ? " " + k : ""),
              query: (null === (n = p.currentPage) || void 0 === n ? void 0 : n.path) ? null === (o = p.currentPage) || void 0 === o ? void 0 : o.query : g.query,
              screenHeight: M(f),
              screenWidth: U(f),
              sdkVersion: s,
              sessionId: u.sessionId,
              title: (null === (r = p.currentPage) || void 0 === r ? void 0 : r.title) || l.getPageTitle(l.getCurrentPage()),
              timestamp: Date.now(),
              timezoneOffset: (new Date).getTimezoneOffset(),
              userId: u.userId
            };
            return a.idMapping && (S.userKey = u.userKey), C(a.ignoreFields) || a.ignoreFields.forEach(e => {
              T(S, e)
            }), C(e) ? S : Object.assign(Object.assign({}, S), e)
          }
        }
      }

      function ae(e, t, i, n) {
        return new(i || (i = Promise))(function (o, r) {
          function s(e) {
            try {
              c(n.next(e))
            } catch (e) {
              r(e)
            }
          }

          function a(e) {
            try {
              c(n.throw(e))
            } catch (e) {
              r(e)
            }
          }

          function c(e) {
            var t;
            e.done ? o(e.value) : (t = e.value, t instanceof i ? t : new i(function (e) {
              e(t)
            })).then(s, a)
          }
          c((n = n.apply(e, t || [])).next())
        })
      }
      "function" == typeof SuppressedError && SuppressedError;
      class ce {
        constructor(e) {
          this.growingIO = e, this.main = (e, t) => {
            var i, n;
            const o = Date.now(),
              {
                emitter: r,
                userStore: s,
                vdsConfig: a,
                platformConfig: c,
                uploader: l,
                dataStore: u,
                dataStore: {
                  shareOut: h,
                  keepAlive: p,
                  lastCloseTime: d,
                  eventHooks: g,
                  saveStorageInfo: f
                }
              } = this.growingIO;
            r.emit("minipLifecycle", {
              event: "App " + e,
              timestamp: o,
              params: null !== (i = t[0]) && void 0 !== i ? i : {}
            }), a.debug && console.log("App:", e, o);
            const m = c.listeners.app;
            switch (r.emit("onComposeBefore", {
                event: "App " + e,
                params: null !== (n = t[0]) && void 0 !== n ? n : {}
              }), e) {
              case m.appCreate:
              case m.appShow: {
                const {
                  path: e,
                  query: i
                } = this.enterParamsParse(t[0]);
                !h && a.originalSource && u.setOriginalSource({
                  path: e,
                  query: i
                }), d ? (Date.now() - d > p || u.lastScene && u.scene !== u.lastScene) && (s.sessionId = "", g.currentPage.time = void 0, this.buildVisitEvent({
                  path: e,
                  query: i
                })) : (this.growingIO.dataStore.lastVisitEvent = {
                  path: e,
                  query: i
                }, this.buildVisitEvent({
                  path: e,
                  query: i
                }));
                break
              }
              case m.appClose:
                u.lastScene = u.scene, u.lastCloseTime = Date.now(), f(), s.saveUserInfo(), this.buildCloseEvent(), a.forceLogin || l.initiateRequest(!0)
            }
          }, this.enterParamsParse = e => {
            const {
              gioPlatform: t,
              minipInstance: i,
              dataStore: n
            } = this.growingIO;
            let o = "",
              r = "";
            const s = (e, t = {}) => {
              o = e, r = k(t).map(e => "".concat(e, "=").concat(t[e])).join("&")
            };
            if ("quickapp" !== t && i.minip.canIUse("getEnterOptionsSync")) {
              const {
                path: t,
                query: o,
                scene: c,
                referrerInfo: l
              } = i.minip.getEnterOptionsSync() || {}, u = e.query || o;
              if (s(e.path || t, u), n.scene = e.scene || c, !C(l) && a(null == l ? void 0 : l.extraData)) {
                let e = [];
                S(l.extraData, (t, i) => {
                  !b(u, i) && ["string", "number", "boolean"].includes(O(t)) && e.push("".concat(i, "=").concat(t))
                });
                const t = e.join("&");
                r = r && t ? "".concat(r, "&").concat(t) : r || t
              }
            } else {
              const {
                path: t,
                query: i
              } = e;
              s(t, i), this.parseScene(e)
            }
            return {
              path: o,
              query: r
            }
          }, this.parseScene = e => {
            var t;
            const {
              minipInstance: i,
              gioPlatform: n,
              dataStore: o
            } = this.growingIO;
            let r;
            if ("quickapp" === n) {
              const {
                extra: e,
                type: t
              } = i.getAppSource();
              r = (null == e ? void 0 : e.scene) || t
            } else C(e) || ((null === (t = null == e ? void 0 : e.query) || void 0 === t ? void 0 : t.wxShoppingListScene) ? r = e.query.wxShoppingListScene : (null == e ? void 0 : e.scene) ? r = e.scene : o.scene = "NA");
            o.scene = r
          }, this.buildVisitEvent = e => {
            const {
              dataStore: t,
              vdsConfig: i,
              minipInstance: o
            } = this.growingIO, {
              originalSourceName: r,
              getOriginalSource: s,
              eventContextBuilder: a,
              eventInterceptor: c
            } = t, l = s(), u = (null == e ? void 0 : e.query) || "";
            let h = Object.assign({
              eventType: "VISIT"
            }, a({
              path: (null == e ? void 0 : e.path) || "",
              query: "string" === O(u) ? u : $(u)
            }));
            i.originalSource && !n(l) && (h = Object.assign(Object.assign({}, h), l), i.dataCollect && o.removeStorageSync(r)), c(h)
          }, this.buildCloseEvent = () => {
            const {
              dataStore: {
                eventContextBuilder: e,
                eventInterceptor: t
              }
            } = this.growingIO;
            t(Object.assign({
              eventType: "APP_CLOSED"
            }, e()))
          }
        }
      }
      class le {
        constructor(e) {
          this.growingIO = e, this.parsePage = (e, t) => {
            var i;
            const n = e.route || e.uri || e.__route__ || (null === (i = null == e ? void 0 : e.$page) || void 0 === i ? void 0 : i.fullPath) || "";
            C(t) ? this.query = void 0 : this.query = this.getQuery(t), this.path !== n && (this.time = Date.now()), this.path = n, this.title = this.settedTitle[this.path] || this.growingIO.minipInstance.getPageTitle(e || this.growingIO.minipInstance.getCurrentPage())
          }, this.getQuery = e => {
            const t = Object.assign({}, e);
            return T(t, "wxShoppingListScene"), $(t)
          }, this.getReferralPage = () => {
            const {
              minipInstance: e,
              dataStore: {
                lastPageEvent: t,
                scene: i
              }
            } = this.growingIO;
            return (null == t ? void 0 : t.path) || (i ? "scn:".concat(e.scnPrefix).concat(i) : null)
          }, this.saveShareId = e => {
            (null == e ? void 0 : e.gioShareId) && (this.queryShareId = e.gioShareId)
          }, this.updateShareResult = e => {
            const [t, i] = this.buildShareQuery(e);
            return e.path = L(t + (i ? "?" + i : "")), e.query = i, e
          }, this.updateAppMessageResult = this.updateShareResult, this.updateTimelineResult = this.updateShareResult, this.updateAddFavoritesResult = e => {
            const [t, i] = this.buildShareQuery(e);
            return e.path = L(t + (i ? "?" + i : "")), e.query = i, e
          }, this.query = void 0, this.settedTitle = {}, this.pageProps = {}
        }
        buildShareQuery(e) {
          var t, i, n;
          const o = F(null !== (t = e.path) && void 0 !== t ? t : "");
          let r = this.path,
            s = {},
            a = b(e, "path");
          return a && (r = u(o), s = Y(h(o)) || {}), C(s) && (s = Y(null !== (i = e.query) && void 0 !== i ? i : "") || {}), !a && C(s) && (s = Y(null !== (n = this.query) && void 0 !== n ? n : "") || {}), [r, $(s)]
        }
      }
      class ue {
        constructor(e) {
          this.growingIO = e, this.main = (e, t, i) => {
            var n, o;
            const r = Date.now(),
              {
                emitter: s,
                minipInstance: a,
                plugins: l,
                vdsConfig: u,
                platformConfig: h,
                dataStore: {
                  shareOut: p,
                  eventHooks: d,
                  toggleShareOut: g,
                  buildAppMessageEvent: f,
                  buildTimelineEvent: m,
                  buildAddFavorites: y
                },
                inPlugin: v
              } = this.growingIO,
              {
                currentPage: _
              } = d;
            if (this.prevEvent[t] && 50 > Date.now() - Number(this.prevEvent[t])) return;
            e || (e = a.getCurrentPage()), e.route || (e.route = a.getCurrentPath(e));
            const b = e.route || e.uri || e.__route__ || (null === (n = null == e ? void 0 : e.$page) || void 0 === n ? void 0 : n.fullPath) || "";
            s.emit("minipLifecycle", {
              event: "Page " + t,
              timestamp: r,
              params: {
                page: e,
                args: i[0]
              }
            }), u.debug && console.log("Page:", b, "#", t, r), this.prevEvent[t] = Date.now();
            const k = h.listeners.page;
            switch (s.emit("onComposeBefore", {
                page: e,
                event: "Page " + t,
                params: {
                  page: e,
                  args: i[0]
                }
              }), _.lastLifecycle = _.currentLifecycle, _.currentLifecycle = t, t) {
              case k.pageLoad:
                this.argQuery[b] = w(e, "options") || w(e, "__displayReporter.query") || w(e, "$page.query") || w(e, "$wx.__displayReporter.query") || i[0] || {}, T(this.argQuery[b], "$taroTimestamp"), _.parsePage(e, this.argQuery[b]);
                break;
              case k.pageShow:
                v ? (_.parsePage(e, this.argQuery[b]), _.path || (_.path = "/插件".concat(u.appId, "}"), _.title = "/插件".concat(u.appId, "}")), this.buildPageEvent()) : p && d.currentPage.time || (_.parsePage(e, this.argQuery[b]), d.currentPage.time = Date.now(), this.buildPageEvent()), g(!1), _.saveShareId(this.argQuery[b]);
                break;
              case k.pageHide:
              case k.pageUnload:
                break;
              case k.shareApp:
                g(!0), u.followShare && f(i);
                break;
              case k.shareTime:
                u.followShare && m(i);
                break;
              case k.addFavorites:
                y(i);
                break;
              case k.tabTap: {
                const e = null === (o = null == l ? void 0 : l.gioEventAutoTracking) || void 0 === o ? void 0 : o.buildTabClickEvent;
                u.autotrack && e && c(e) && e(i[0]);
                break
              }
            }
            t === k.pageUnload && (_.pageProps[b] = void 0)
          }, this.buildPageEvent = e => {
            var t;
            const {
              dataStore: {
                eventContextBuilder: i,
                eventInterceptor: n,
                eventHooks: o
              }
            } = this.growingIO, {
              currentPage: r
            } = o, s = Object.assign(Object.assign({
              eventType: "PAGE",
              referralPage: r.getReferralPage()
            }, i()), {
              timestamp: r.time
            });
            C(r.pageProps[s.path]) || (s.attributes = r.pageProps[s.path]), !C(e) && e.path && (s.path = e.path, s.query = e.query, s.title = null !== (t = e.title) && void 0 !== t ? t : s.title), n(s)
          }, this.prevEvent = {}, this.argQuery = {}
        }
      }
      class he {
        constructor(e) {
          var t, i;
          this.growingIO = e, this.isNormalFc = (e, t) => c(t) && "constructor" !== e, this.objectTraverse = (e, t) => {
            Object.getOwnPropertyNames(e).forEach(i => t(i, e)), b(e, "methods") && Object.getOwnPropertyNames(e.methods).forEach(i => {
              e[i] || t(i, e.methods)
            }), b(e, "lifetimes") && Object.getOwnPropertyNames(e.lifetimes).forEach(i => {
              e[i] || t(i, e.lifetimes)
            }), b(e, "pageLifetimes") && Object.getOwnPropertyNames(e.pageLifetimes).forEach(i => {
              e[i] || t(i, e.pageLifetimes)
            })
          }, this.supLifeFcs = (e, t) => {
            l(this[t + "Handlers"]) && this[t + "Handlers"].forEach(t => {
              c(e[t]) || ["onShareAppMessage", "onShareTimeline"].includes(t) || (e[t] = () => {})
            })
          }, this.lifeFcEffects = (e, t, i) => {
            const n = this;
            return ["onShareTimeline", "onAddToFavorites"].includes(e) ? function (...o) {
              let r = t.apply(this, o);
              "onShareTimeline" === e && n.growingIO.vdsConfig.followShare && (r = n.currentPage.updateTimelineResult(null != r ? r : {})), "onAddToFavorites" === e && (r = n.currentPage.updateAddFavoritesResult(null != r ? r : {}));
              const s = [].slice.call(o);
              return r && s.push(r), n["def".concat(i, "Cbs")][e].apply(this, s), r
            } : function (...o) {
              var r;
              return ae(this, void 0, void 0, function* () {
                let s;
                try {
                  if ("onShareAppMessage" === e) {
                    if (s = null !== (r = yield t.apply(this, o)) && void 0 !== r ? r : {}, "promise" === O(s.promise)) {
                      const e = function () {
                        return ae(this, void 0, void 0, function* () {
                          let e = s;
                          return new Promise(t => {
                            let i = setTimeout(() => {
                              t(Object.assign({}, e)), clearTimeout(i), i = void 0
                            }, 3e3);
                            s.promise.then(n => {
                              e = n, t(Object.assign({}, e)), clearTimeout(i), i = void 0
                            })
                          })
                        })
                      };
                      s = Object.assign(Object.assign({}, s), yield e()), T(s, "promise")
                    }
                    n.growingIO.vdsConfig.followShare && (s = n.currentPage.updateAppMessageResult(null != s ? s : {}))
                  }
                  const a = [].slice.call(o);
                  s && a.push(s), n["def".concat(i, "Cbs")][e].apply(this, a)
                } catch (e) {
                  A(e, "error")
                }
                return "onShareAppMessage" !== e && (s = t.apply(this, o)), n.growingIO.emitter.emit("minipLifecycle", {
                  event: "".concat(i, " ").concat(e, "End"),
                  timestamp: Date.now(),
                  params: {
                    instance: this,
                    arguments: Array.from(o)
                  }
                }), s
              })
            }
          }, this.customFcEffects = (e, t) => {
            const i = this;
            return function (...n) {
              var o, r;
              let s;
              if (i.growingIO.vdsConfig.autotrack && i.growingIO.plugins.gioEventAutoTracking) try {
                let t = n[0] || {};
                b(t, "type") && ((null == t ? void 0 : t.currentTarget) || (null == t ? void 0 : t.target)) || (t = n[n.length - 1]), ((null == t ? void 0 : t.currentTarget) || (null == t ? void 0 : t.target)) && i.actionEventTypes.includes(t.type) && (c(i.actionEffects) || (i.actionEffects = (null === (r = null === (o = i.growingIO.plugins) || void 0 === o ? void 0 : o.gioEventAutoTracking) || void 0 === r ? void 0 : r.main) || function () {}), null == i || i.actionEffects(t, e))
              } catch (e) {
                A(e, "error")
              }
              return s = t.apply(this, n), s
            }
          }, this.appApplyProxy = (e, t) => this.appHandlers.includes(e) ? this.lifeFcEffects(e, t, "App") : this.customFcEffects(e, t), this.pageApplyProxy = (e, t) => this.pageHandlers.includes(e) ? this.lifeFcEffects(e, t, "Page") : this.customFcEffects(e, t), this.appOverriding = e => (this.setAppEffectCbs(), this.supLifeFcs(e, "app"), this.objectTraverse(e, (e, t) => {
            this.isNormalFc(e, t[e]) && (t[e] = this.appApplyProxy(e, t[e]))
          }), e), this.pageOverriding = e => (this.setPageEffectCbs(), this.supLifeFcs(e, "page"), this.objectTraverse(e, (e, t) => {
            this.isNormalFc(e, t[e]) && (t[e] = this.pageApplyProxy(e, t[e]))
          }), e), this.componentOverriding = e => (this.setPageEffectCbs(), e.methods || (e.methods = {}), this.supLifeFcs(this.growingIO.inPlugin ? e : e.methods, "page"), this.objectTraverse(this.growingIO.inPlugin ? e : e.methods, (e, t) => {
            this.isNormalFc(e, t[e]) && (t[e] = this.pageApplyProxy(e, t[e]))
          }), e), this.setAppEffectCbs = () => {
            const e = this;
            this.appHandlers.forEach(t => {
              this.defAppCbs[t] = function (...i) {
                e.appEffects.main(t, i)
              }
            })
          }, this.setPageEffectCbs = () => {
            const e = this;
            this.pageHandlers.forEach(t => {
              this.defPageCbs[t] = function (...i) {
                e.pageEffects.main(this, t, i)
              }
            })
          }, this.growingApp = e => this.originalApp(this.appOverriding(e)), this.growingPage = e => this.originalPage(this.pageOverriding(e)), this.growingComponent = e => this.originalComponent(this.componentOverriding(e)), this.growingBehavior = e => this.originalBehavior(this.componentOverriding(e)), this.nativeGrowing = (e = ["App", "Page", "Component", "Behavior"]) => {
            const t = this,
              {
                platformConfig: i
              } = this.growingIO,
              n = i.hooks;
            if (this.setAppEffectCbs(), this.setPageEffectCbs(), e.includes("App")) try {
              n.App && !this.appHooked && (App = function (...e) {
                return t.growingApp(e[0])
              }, this.appHooked = !0)
            } catch (e) {}
            if (e.includes("Page")) try {
              n.Page && !this.pageHooked && (Page = function (...e) {
                return t.growingPage(e[0])
              }, this.pageHooked = !0)
            } catch (e) {}
            if (e.includes("Component")) try {
              n.Component && !this.componentHooked && (Component = function (...e) {
                return t.growingComponent(e[0])
              }, this.componentHooked = !0)
            } catch (e) {}
            if (e.includes("Behavior")) try {
              n.Behavior && !this.behaviorHooked && (Behavior = function (...e) {
                return t.growingBehavior(e[0])
              }, this.behaviorHooked = !0)
            } catch (e) {}
          }, this.initEventHooks = () => {
            const e = this,
              {
                platformConfig: t,
                gioPlatform: i
              } = this.growingIO;
            t.canHook ? (this.nativeGrowing(), z().GioApp = R(() => null !== App && void 0 !== App ? App : window.GioApp), z().GioPage = R(() => null !== Page && void 0 !== Page ? Page : window.GioPage), z().GioComponent = R(() => null !== Component && void 0 !== Component ? Component : window.GioComponent), z().GioBehavior = R(() => Behavior)) : "quickapp" === i && (window.GioApp = function (...t) {
              return e.appOverriding(t[0])
            }, window.GioPage = function (...t) {
              return e.pageOverriding(t[0])
            }, window.GioComponent = function (...t) {
              return e.pageOverriding(t[0])
            })
          };
          const n = null === (t = this.growingIO) || void 0 === t ? void 0 : t.platformConfig;
          this.defAppCbs = {}, this.defPageCbs = {}, this.appHandlers = n.appHandlers, this.pageHandlers = n.pageHandlers, this.actionEventTypes = n.actionEventTypes, this.originalApp = n.originalApp, this.originalPage = n.originalPage, this.originalComponent = n.originalComponent, this.originalBehavior = null !== (i = n.originalBehavior) && void 0 !== i ? i : function () {}, this.appEffects = new ce(this.growingIO), this.pageEffects = new ue(this.growingIO), this.currentPage = new le(this.growingIO)
        }
      }
      class pe {
        constructor(e) {
          var t, i;
          this.growingIO = e, this.ALLOW_SETTING_KEYS = k(ee), this.gsidStorageName = "_growing_gsid_", this.originalSourceName = "gdp_original_source", this.initStorageInfo = () => {
            const {
              minipInstance: e
            } = this.growingIO, t = V(), i = t.gio_gsid ? t.gio_gsid : Number.parseInt(e.getStorageSync(this.gsidStorageName), 10);
            this._gsid = Number.isNaN(i) || i >= 1e9 || 1 > i ? 1 : i, this._stid = this._gsid, i !== this._gsid && e.setStorageSync(this.gsidStorageName, this._gsid)
          }, this.saveStorageInfo = () => {
            const {
              minipInstance: e
            } = this.growingIO;
            this._stid = this._gsid, J(e, [{
              key: this.gsidStorageName,
              value: this._gsid
            }])
          }, this.setOriginalSource = ({
            path: e,
            query: t
          }) => {
            const {
              minipInstance: i
            } = this.growingIO;
            if (n(this.getOriginalSource())) {
              const n = {
                path: e,
                query: t,
                title: ""
              };
              i.setStorageSync(this.originalSourceName, JSON.stringify(n))
            }
          }, this.getOriginalSource = () => {
            const {
              minipInstance: e
            } = this.growingIO;
            return R(() => JSON.parse(e.getStorageSync(this.originalSourceName)))
          }, this.initOptions = e => {
            var t, i, n, o, r, s, a, c;
            const {
              projectId: u,
              dataSourceId: h,
              appId: p
            } = e, d = {};
            this.ALLOW_SETTING_KEYS.forEach(t => {
              const i = ee[t].type;
              (l(i) ? i.includes(O(e[t])) : O(e[t]) === ee[t].type) ? "ignoreFields" === t ? d.ignoreFields = e.ignoreFields.filter(e => oe.includes(e)) : "extraParams" === t ? d.extraParams = e.extraParams.filter(e => re.includes(e)) : d[t] = e[t]: d[t] = ee[t].default
            }), d.uploadInterval = Math.round(d.uploadInterval), (Number.isNaN(d.uploadInterval) || 0 > d.uploadInterval || d.uploadInterval > 2e3) && (d.uploadInterval = 1e3), d.enableIdMapping && !d.idMapping && (d.idMapping = !0), d.pluginMode && (this.growingIO.inPlugin = !0), this.growingIO.vdsConfig = Object.assign(Object.assign({}, d), {
              projectId: u,
              dataSourceId: h,
              appId: p,
              performance: {
                monitor: null === (i = null === (t = d.performance) || void 0 === t ? void 0 : t.monitor) || void 0 === i || i,
                exception: null === (o = null === (n = d.performance) || void 0 === n ? void 0 : n.exception) || void 0 === o || o,
                network: null !== (s = null === (r = d.performance) || void 0 === r ? void 0 : r.network) && void 0 !== s && s
              }
            }), this.keepAlive = d.keepAlive, d.dataCollect || A("已关闭数据采集", "info"), d.autotrack || A("已关闭无埋点", "info");
            const {
              plugins: g,
              inPlugin: f,
              minipInstance: m
            } = this.growingIO, {
              uniVue: y,
              taro: v
            } = d;
            y || v || (this.growingIO.platformConfig.canHook = !0), f && !["tbp", "jdp"].includes(m.platform) || this.eventHooks.initEventHooks(), y && (null === (a = null == g ? void 0 : g.gioUniAppAdapter) || void 0 === a || a.main()), v && (null === (c = null == g ? void 0 : g.gioTaroAdapter) || void 0 === c || c.main())
          }, this.setOption = (e, t) => {
            var i;
            const {
              vdsConfig: n,
              userStore: r,
              uploader: s,
              emitter: a
            } = this.growingIO, c = o(e) && this.ALLOW_SETTING_KEYS.includes(e), l = c && typeof t === (null === (i = ee[e]) || void 0 === i ? void 0 : i.type);
            if (c && l) {
              if ("dataCollect" === e && !1 === n.dataCollect && !0 === t) {
                let e = setTimeout(() => {
                  r.sessionId = "";
                  const {
                    path: t,
                    query: i,
                    settedTitle: n
                  } = this.eventHooks.currentPage;
                  this.eventHooks.currentPage.title = n[t] || this.growingIO.minipInstance.getPageTitle(this.growingIO.minipInstance.getCurrentPage()), this.sendVisit({
                    path: t,
                    query: i
                  }), this.eventHooks.currentPage.time = Date.now(), this.sendPage({
                    path: t,
                    query: i
                  }), clearTimeout(e), e = null
                }, 0)
              }
              return n[e] = t, "serverUrl" === e && (null == s || s.generateURL()), a.emit("OPTION_CHANGE", {
                optionName: e,
                optionValue: t
              }), !0
            }
            return E("setOption > " + e), !1
          }, this.getOption = e => {
            const {
              vdsConfig: t
            } = this.growingIO;
            return e && b(t, f(e)) ? t[f(e)] : n(e) ? Object.assign({}, t) : void E("getOption > " + e)
          }, this.toggleShareOut = e => {
            s(e) ? this.shareOut = e : this.shareOut = !this.shareOut
          }, this.sendVisit = e => {
            this.eventHooks.appEffects.buildVisitEvent(null != e ? e : this.lastVisitEvent), this.eventHooks.currentPage.time = Date.now()
          }, this.sendPage = e => {
            this.eventHooks.pageEffects.buildPageEvent(e)
          }, this.eventConverter = e => {
            const {
              vdsConfig: t,
              dataStore: i,
              uploader: n
            } = this.growingIO;
            if (t.dataCollect) {
              ["LOGIN_USER_ATTRIBUTES", "APP_CLOSED"].includes(e.eventType) || (e.eventSequenceId = i.gsid, this.growingIO.dataStore.gsid += 1);
              const t = {};
              S(e, (e, i) => {
                var n;
                if ("element" === i) {
                  const i = null !== (n = u(e)) && void 0 !== n ? n : {};
                  S(i, (e, i) => {
                    C(e) && 0 !== e || (t[i] = e)
                  })
                } else C(e) && 0 !== e || (t[i] = e)
              }), this.growingIO.emitter.emit("onComposeAfter", {
                composedEvent: t
              }), n.commitRequest(Object.assign(Object.assign({}, t), {
                requestId: q()
              }))
            }
          }, this.eventInterceptor = e => {
            const {
              systemInfo: t,
              network: i
            } = this.growingIO.minipInstance;
            C(t) || C(i) ? this.interceptEvents.push(e) : C(this.interceptEvents) ? this.eventConverter(e) : ([...this.interceptEvents, e].forEach(e => {
              const t = Object.assign(Object.assign({}, e), this.eventContextBuilder({
                path: e.path,
                query: e.query,
                timestamp: e.timestamp
              }));
              this.eventConverter(t)
            }), this.interceptEvents = [])
          }, this.eventReleaseInspector = () => {
            const {
              minipInstance: {
                systemInfo: e,
                network: t
              }
            } = this.growingIO;
            e && t && !C(this.interceptEvents) && ([...this.interceptEvents].forEach(e => {
              const t = Object.assign(Object.assign({}, e), this.eventContextBuilder({
                path: e.path,
                query: e.query,
                timestamp: e.timestamp
              }));
              this.eventConverter(t)
            }), this.interceptEvents = [])
          }, this.buildAppMessageEvent = e => {
            var t;
            const i = e[0];
            let n;
            2 > e.length ? 1 === e.length && (n = i) : n = e[1];
            const {
              dataStore: {
                eventContextBuilder: o,
                eventInterceptor: r
              }
            } = this.growingIO, s = ((null == n ? void 0 : n.path) || "").split("?");
            r(Object.assign({
              eventType: "CUSTOM",
              eventName: "$mp_on_share",
              attributes: Object.assign({
                $from: i.from,
                $target: null === (t = null == i ? void 0 : i.target) || void 0 === t ? void 0 : t.id,
                $share_title: null == n ? void 0 : n.title,
                $share_path: u(s),
                $share_query: s[1]
              }, null == n ? void 0 : n.attributes)
            }, o()))
          }, this.buildTimelineEvent = e => {
            var t;
            const i = e[0];
            let n;
            2 > e.length ? 1 === e.length && (n = i) : n = e[1];
            const {
              dataStore: {
                eventContextBuilder: o,
                eventInterceptor: r
              }
            } = this.growingIO, s = ((null == n ? void 0 : n.path) || "").split("?");
            r(Object.assign({
              eventType: "CUSTOM",
              eventName: "$mp_share_timeline",
              attributes: Object.assign({
                $target: null === (t = null == i ? void 0 : i.target) || void 0 === t ? void 0 : t.id,
                $share_title: null == n ? void 0 : n.title,
                $share_path: u(s),
                $share_query: s[1]
              }, null == n ? void 0 : n.attributes)
            }, o()))
          }, this.buildAddFavorites = e => {
            const t = e[0];
            let i;
            2 > e.length ? 1 === e.length && (i = t) : i = e[1];
            const {
              dataStore: {
                eventContextBuilder: n,
                eventInterceptor: o
              }
            } = this.growingIO, r = ((null == i ? void 0 : i.path) || "").split("?");
            o(Object.assign({
              eventType: "CUSTOM",
              eventName: "$mp_add_favorites",
              attributes: {
                $share_title: null == i ? void 0 : i.title,
                $share_path: u(r),
                $share_query: r[1]
              }
            }, n()))
          }, this.initStorageInfo(), this.eventContextBuilder = new se(this.growingIO).main, this.shareOut = !1, this.lastVisitEvent = {}, this.lastPageEvent = {}, this.locationData = {}, this.generalProps = {}, this.trackTimers = {}, this.interceptEvents = [], this.eventHooks = new he(this.growingIO), this.growingIO.emitter.on("onComposeAfter", ({
            composedEvent: e
          }) => {
            "VISIT" !== e.eventType && "vst" !== e.t || (this.lastVisitEvent = e), "PAGE" !== e.eventType && "page" !== e.t || (this.lastPageEvent = e)
          }), c(null === (t = this.growingIO.minipInstance.minip) || void 0 === t ? void 0 : t.onAppHide) && this.growingIO.minipInstance.minip.onAppHide(() => {
            S(this.trackTimers, e => {
              e.start && (e.leng = e.leng + (+Date.now() - e.start))
            })
          }), c(null === (i = this.growingIO.minipInstance.minip) || void 0 === i ? void 0 : i.onAppShow) && this.growingIO.minipInstance.minip.onAppShow(() => {
            S(this.trackTimers, e => {
              e.start && (e.start = +Date.now())
            })
          }), this.growingIO.emitter.on("OPTION_CHANGE", ({
            optionName: e,
            optionValue: t
          }) => {
            "dataCollect" === e && !1 === t && this.growingIO.clearTrackTimer()
          })
        }
        get gsid() {
          const e = V(),
            t = W(e);
          return !C(t) && e.gio_gsid ? e.gio_gsid : this._gsid
        }
        set gsid(e) {
          const t = Number.parseInt(e, 10);
          this._gsid = Number.isNaN(t) || e >= 1e9 || 1 > e ? 1 : e, V().gio_gsid = this._gsid, 10 > this._gsid - this._stid || this.saveStorageInfo()
        }
        get scene() {
          return this._scene
        }
        set scene(e) {
          const t = this._scene;
          this._scene = e, t !== this._scene && this.growingIO.emitter.emit("SCENE_UPDATE", {
            newScene: e,
            oldScene: t
          })
        }
      }
      const de = {
          scnPrefix: "",
          appHandlers: ["onLaunch", "onShow", "onHide", "onError", "onPageNotFound", "onUnhandledRejection", "onThemeChange"],
          pageHandlers: ["onLoad", "onShow", "onReady", "onHide", "onShareAppMessage", "onTabItemTap", "onUnload", "onPullDownRefresh", "onReachBottom", "onResize"],
          actionEventTypes: ["onclick", "tap", "onTap", "longpress", "longTap", "blur", "change", "onChange", "submit", "confirm", "getuserinfo", "getphonenumber", "contact", "mouseup"],
          originalApp: R(() => App),
          originalPage: R(() => Page),
          originalComponent: R(() => Component),
          originalBehavior: R(() => Behavior),
          canHook: !0,
          hooks: {
            App: !0,
            Page: !0,
            Component: !0,
            Behavior: !0
          },
          listeners: {
            app: {
              appLaunch: "onLaunch",
              appShow: "onShow",
              appClose: "onHide"
            },
            page: {
              pageLoad: "onLoad",
              pageShow: "onShow",
              pageReady: "onReady",
              pageHide: "onHide",
              pageUnload: "onUnload",
              tabTap: "onTabItemTap",
              shareApp: "onShareAppMessage"
            },
            actions: {
              click: ["onclick", "tap", "longpress", "longTap", "getuserinfo", "getphonenumber", "contact", "mouseup"],
              change: ["blur", "change", "confirm"],
              submit: ["submit"]
            }
          }
        },
        ge = Object.assign(Object.assign({}, de), {
          listeners: Object.assign({}, de.listeners),
          name: "Weixin",
          platform: "MinP"
        });
      ge.pageHandlers = [...de.pageHandlers, "onShareTimeline", "onAddToFavorites"], ge.listeners.page = Object.assign(Object.assign({}, de.listeners.page), {
        shareTime: "onShareTimeline",
        addFavorites: "onAddToFavorites"
      });
      class fe {
        constructor(e) {
          this.growingIO = e, this.minip = G("wx"), this.hookSetTitle = () => {
            var e;
            const t = null === (e = this.minip) || void 0 === e ? void 0 : e.setNavigationBarTitle,
              i = this;
            t && Object.defineProperty(this.minip, "setNavigationBarTitle", {
              writable: !0,
              enumerable: !0,
              configurable: !0,
              value: function () {
                if (i.growingIO.gioSDKInitialized) {
                  const e = i.getCurrentPath(),
                    {
                      title: t
                    } = arguments[0] || {};
                  i.growingIO.dataStore.eventHooks.currentPage.settedTitle[e] = t
                }
                return t.apply(this, arguments)
              }
            })
          }, this.navigateTo = e => {
            var t;
            return null === (t = this.minip) || void 0 === t ? void 0 : t.navigateTo(e)
          }, this.switchTab = e => {
            var t;
            null === (t = this.minip) || void 0 === t || t.switchTab(e)
          }, this.navigateToMiniProgram = e => {
            var t;
            return null === (t = this.minip) || void 0 === t ? void 0 : t.navigateToMiniProgram(e)
          }, this.getImageInfo = ({
            src: e,
            success: t,
            fail: i,
            complete: n
          }) => {
            var o;
            return null === (o = this.minip) || void 0 === o ? void 0 : o.getImageInfo({
              src: e,
              success: t,
              fail: i,
              complete: n
            })
          }, this.initImpression = e => {
            var t, i;
            null === (i = null === (t = this.growingIO.plugins) || void 0 === t ? void 0 : t.gioImpressionTracking) || void 0 === i || i.main(e, "observeAll")
          }, this.getCurrentPage = () => R(() => h(getCurrentPages())) || {}, this.getCurrentPath = () => {
            const e = this.getCurrentPage();
            return (null == e ? void 0 : e.route) || (null == e ? void 0 : e.uri) || (null == e ? void 0 : e.__route__) || ""
          }, this.getPageTitle = e => {
            var t, i;
            let n = "";
            const r = B(H());
            try {
              const s = (null == e ? void 0 : e.data) || e.$data || {};
              if (n = o(null == s ? void 0 : s.gioPageTitle) ? null == s ? void 0 : s.gioPageTitle : "", 0 === n.length) {
                const t = r.page[e.route] || r.page[e.route + ".html"];
                n = t ? t.window.navigationBarTitleText : r.global.window.navigationBarTitleText
              }
              if (0 === n.length) {
                const o = null === (i = null === (t = null == r ? void 0 : r.tabBar) || void 0 === t ? void 0 : t.list) || void 0 === i ? void 0 : i.find(t => t.pagePath === e.route || t.pagePath === e.route + ".html");
                n = (null == o ? void 0 : o.text) || ""
              }
            } catch (e) {
              return ""
            }
            return N(n)
          }, this.getStorageSync = e => {
            var t;
            let i = null === (t = this.minip) || void 0 === t ? void 0 : t.getStorageSync(e);
            return a(i) && i.expiredAt ? i.expiredAt < Date.now() ? "" : i.value : i
          }, this.getStorage = e => new Promise(t => {
            var i;
            null === (i = this.minip) || void 0 === i || i.getStorage({
              key: e,
              success: ({
                data: e
              }) => t(e),
              fail: () => t("")
            })
          }), this.setStorageSync = (e, t, i) => {
            var n;
            i && (t = {
              value: t,
              expiredAt: i
            }), null === (n = this.minip) || void 0 === n || n.setStorageSync(e, t)
          }, this.setStorage = (e, t) => {
            var i;
            null === (i = this.minip) || void 0 === i || i.setStorage({
              key: e,
              data: t
            })
          }, this.removeStorageSync = e => {
            var t;
            null === (t = this.minip) || void 0 === t || t.removeStorageSync(e)
          }, this.removeStorage = e => {
            var t;
            null === (t = this.minip) || void 0 === t || t.removeStorage(e)
          }, this.getNetworkType = () => {
            const e = this;
            return new Promise(t => {
              var i;
              null === (i = this.minip) || void 0 === i || i.getNetworkType({
                success: i => {
                  e.network = i, t(i)
                },
                fail: () => t(null)
              })
            })
          }, this.request = ({
            url: e,
            data: t,
            header: i,
            timeout: n,
            method: o,
            success: r,
            fail: s,
            complete: a
          }) => {
            var l;
            const u = null === (l = this.minip) || void 0 === l ? void 0 : l.request({
              url: e,
              data: t,
              header: i,
              headers: i,
              timeout: n,
              method: o,
              success: r,
              fail: s,
              complete: a
            });
            let h = setTimeout(() => {
              (null == u ? void 0 : u.abort) && c(null == u ? void 0 : u.abort) && (null == u || u.abort()), clearTimeout(h), h = null
            }, (n || 1e4) + 10);
            return u
          }, this.getSystemInfo = () => {
            const e = this;
            return new Promise(t => {
              var i;
              null === (i = this.minip) || void 0 === i || i.getSystemInfo({
                success: i => {
                  e.systemInfo = i, t(i)
                },
                fail: () => t(null)
              })
            })
          }, this.getSetting = () => new Promise(e => {
            var t;
            null === (t = this.minip) || void 0 === t || t.getSetting({
              success: e,
              fail: e
            })
          });
          const {
            platformConfig: {
              platform: t,
              scnPrefix: i
            }
          } = this.growingIO;
          this.platform = t, this.scnPrefix = i, this.growingIO.emitter.on("OPTION_INITIALIZED", () => {
            this.getNetworkType().then(() => {
              var e;
              return null === (e = this.growingIO.dataStore) || void 0 === e ? void 0 : e.eventReleaseInspector()
            }), this.getSystemInfo().then(() => {
              var e;
              return null === (e = this.growingIO.dataStore) || void 0 === e ? void 0 : e.eventReleaseInspector()
            })
          })
        }
      }
      class me extends fe {
        constructor(e) {
          super(e), this.growingIO = e, this.hookSetTitle()
        }
      }
      let ye;
      const ve = {};
      var _e, be, ke;
      be = {
        name: "gioCustomTracking",
        method: class {
          constructor(e) {
            this.growingIO = e, this.getDynamicAttributes = e => (ye.isNil(e) || ye.keys(e).forEach(t => {
              ye.isFunction(e[t]) ? e[t] = e[t]() : ye.isArray(e[t]) || (e[t] = ye.toString(e[t]))
            }), e), this.buildCustomEvent = (e, t) => {
              ye.eventNameValidate(e, () => {
                const {
                  dataStore: {
                    eventContextBuilder: i,
                    eventInterceptor: n
                  }
                } = this.growingIO;
                n(Object.assign({
                  eventType: "CUSTOM",
                  eventName: e,
                  attributes: ye.limitObject(this.getDynamicAttributes(ye.isObject(t) && !ye.isEmpty(t) ? t : void 0))
                }, i()))
              })
            }, this.buildUserAttributesEvent = e => {
              const {
                dataStore: {
                  eventContextBuilder: t,
                  eventInterceptor: i,
                  lastVisitEvent: n
                }
              } = this.growingIO, o = Object.assign({
                eventType: "LOGIN_USER_ATTRIBUTES",
                attributes: ye.limitObject(e)
              }, t());
              o.path || (o.path = n.path, o.query = n.query, o.title = n.title), i(o)
            }, ye = this.growingIO.utils
          }
        }
      }, ke = ve, (_e = ["pluginsIn", "gioCustomTracking"]).map(function (e, t) {
        ke[e] = t == _e.length - 1 ? be : ke[e] || {}, ke = ke[e]
      });
      class Se {
        constructor(e) {
          this.growingIO = e, this.innerPluginInit = () => {
            k(ve.pluginsIn).forEach(e => {
              const {
                name: t,
                method: i
              } = ve.pluginsIn[e];
              this.pluginItems.find(e => e.name === t) || this.pluginItems.push({
                name: y(t || e),
                method: i || (e => {})
              })
            }), C(this.pluginItems) || this.installAll()
          }, this.install = (e, t, i) => {
            var n;
            const o = t || this.pluginItems.find(t => t.name === e);
            if (null === (n = this.growingIO) || void 0 === n ? void 0 : n.plugins[e]) return A("重复加载插件 ".concat(e, " 或插件重名，已跳过加载!"), "warn"), !1;
            if (!o) return A("插件加载失败!不存在名为 ".concat(e, " 的插件!"), "error"), !1;
            try {
              return this.growingIO.plugins[e] = new o.method(this.growingIO, i), t && A("加载插件：" + e, "info"), !0
            } catch (t) {
              return A("插件【".concat(e, "】加载异常 ").concat(t), "error"), !1
            }
          }, this.installAll = e => {
            (e || this.pluginItems).forEach(t => this.install(t.name, e ? t : void 0, t.options))
          }, this.uninstall = e => {
            var t;
            T(this.pluginItems, e);
            const i = T(null === (t = this.growingIO) || void 0 === t ? void 0 : t.plugins, e);
            return i || A("卸载插件 ".concat(e, " 失败!"), "error"), i
          }, this.uninstallAll = () => {
            this.pluginItems.forEach(e => this.uninstall(e.name))
          }, this.lifeError = (e, t) => A("插件执行错误 ".concat(e.name, " ").concat(t), "error"), this.onComposeBefore = e => {
            this.pluginItems.forEach(t => {
              var i;
              const n = null === (i = this.growingIO.plugins[t.name]) || void 0 === i ? void 0 : i.onComposeBefore;
              if (n && c(n)) try {
                n(e)
              } catch (e) {
                this.lifeError(t, e)
              }
            })
          }, this.onComposeAfter = e => {
            this.pluginItems.forEach(t => {
              var i;
              const n = null === (i = this.growingIO.plugins[t.name]) || void 0 === i ? void 0 : i.onComposeAfter;
              if (n && c(n)) try {
                n(e)
              } catch (e) {
                this.lifeError(t, e)
              }
            })
          }, this.onSendBefore = e => {
            this.pluginItems.forEach(t => {
              var i;
              const n = null === (i = this.growingIO.plugins[t.name]) || void 0 === i ? void 0 : i.onSendBefore;
              if (n && c(n)) try {
                n(e)
              } catch (e) {
                this.lifeError(t, e)
              }
            })
          }, this.onSendAfter = e => {
            this.pluginItems.forEach(t => {
              var i;
              const n = null === (i = this.growingIO.plugins[t.name]) || void 0 === i ? void 0 : i.onSendAfter;
              if (n && c(n)) try {
                n(e)
              } catch (e) {
                this.lifeError(t, e)
              }
            })
          }, this.pluginItems = [], this.growingIO.emitter.on("onComposeBefore", this.onComposeBefore), this.growingIO.emitter.on("onComposeAfter", this.onComposeAfter), this.growingIO.emitter.on("onSendBefore", this.onSendBefore), this.growingIO.emitter.on("onSendAfter", this.onSendAfter)
        }
      }
      var xe = {},
        we = {}.hasOwnProperty;

      function Te(e) {
        try {
          return decodeURIComponent(e.replace(/\+/g, " "))
        } catch (e) {
          return null
        }
      }

      function Ie(e) {
        try {
          return encodeURIComponent(e)
        } catch (e) {
          return null
        }
      }
      xe.stringify = function (e, t) {
        t = t || "";
        var i, n, o = [];
        for (n in "string" != typeof t && (t = "?"), e)
          if (we.call(e, n)) {
            if ((i = e[n]) || null != i && !isNaN(i) || (i = ""), n = Ie(n), i = Ie(i), null === n || null === i) continue;
            o.push(n + "=" + i)
          } return o.length ? t + o.join("&") : ""
      }, xe.parse = function (e) {
        for (var t, i = /([^=?#&]+)=?([^&]*)/g, n = {}; t = i.exec(e);) {
          var o = Te(t[1]),
            r = Te(t[2]);
          null === o || null === r || o in n || (n[o] = r)
        }
        return n
      };
      class Ce {
        constructor(e) {
          this.growingIO = e, this.generateURL = () => {
            const {
              serverUrl: e,
              projectId: t
            } = this.growingIO.vdsConfig;
            return v(e, "http") ? "".concat(e, "/v3/projects/").concat(t, "/collect") : "https://".concat(e, "/v3/projects/").concat(t, "/collect")
          }, this.commitRequest = e => {
            const t = Object.assign({}, e),
              {
                vdsConfig: i
              } = this.growingIO;
            i.forceLogin ? this.hoardingQueue.push(t) : (this.requestQueue.push(t), this.initiateRequest())
          }, this.initiateRequest = e => {
            var t, i;
            const {
              plugins: n,
              vdsConfig: o
            } = this.growingIO;
            [...this.hoardingQueue, ...this.requestQueue].length > 0 && this.requestingNum < this.requestLimit && ((null === (t = null == o ? void 0 : o.tbConfig) || void 0 === t ? void 0 : t.cloudFuncSend) ? null === (i = null == n ? void 0 : n.gioTaobaoAdapter) || void 0 === i || i.singleInvoke() : e ? this.batchInvoke() : this.batchInvokeThrottle())
          }, this.batchInvoke = () => {
            var e, t;
            const {
              vdsConfig: i,
              plugins: n,
              emitter: o
            } = this.growingIO;
            let r = [...this.hoardingQueue, ...this.requestQueue];
            r.length > 50 ? (r = r.slice(0, 50), this.hoardingQueue.length > 50 ? this.hoardingQueue = this.hoardingQueue.slice(50) : (this.hoardingQueue = [], this.requestQueue = this.requestQueue.slice(50 - this.hoardingQueue.length))) : (this.hoardingQueue = [], this.requestQueue = []);
            let s = r.filter(e => (this.retryIds[e.requestId] || 0) <= this.retryLimit);
            if (C(s)) return;
            const a = s.map(e => {
              const t = Object.assign({}, e);
              return T(t, "requestId"), t
            });
            i.debug && console.log("[GrowingIO Debug]:", JSON.stringify(a, null, 2)), o.emit("onSendBefore", {
              requestData: a
            }), (null === (e = null == i ? void 0 : i.tbConfig) || void 0 === e ? void 0 : e.cloudAppId) ? null === (t = null == n ? void 0 : n.gioTaobaoAdapter) || void 0 === t || t.tbCloudAppInvoke(a) : this.normalBatchInvoke(s, a)
          }, this.batchInvokeThrottle = I(this.batchInvoke, this.growingIO.vdsConfig.uploadInterval, !1, !1), this.normalBatchInvoke = (e, t) => {
            var i;
            const {
              minipInstance: n,
              vdsConfig: o,
              emitter: r,
              plugins: s
            } = this.growingIO;
            this.requestingNum += 1;
            const a = {
              "content-type": "jdp" === n.platform ? "application/json" : "application/json;charset=UTF-8"
            };
            let c = [...t];
            const u = o.compress && (null === (i = null == s ? void 0 : s.gioCompress) || void 0 === i ? void 0 : i.compressToUTF16);
            u && (c = s.gioCompress.compressToUTF16(JSON.stringify(t)), a["X-Compress-Codec"] = "1"), n.request({
              url: "".concat(this.requestURL, "?stm=").concat(Date.now(), "&compress=").concat(u ? "1" : "0"),
              header: a,
              method: "POST",
              data: c,
              timeout: this.requestTimeout,
              fail: t => {
                [200, 204].includes(t.code) || (l(e) ? e.forEach(e => {
                  this.requestFailFn(e)
                }) : this.requestFailFn(e), A("请求失败!" + JSON.stringify(t), "error"))
              },
              complete: e => {
                this.requestingNum -= 1, r.emit("onSendAfter", {
                  result: e
                }), this.initiateRequest()
              }
            })
          }, this.requestFailFn = e => {
            this.retryIds[e.requestId] || (this.retryIds[e.requestId] = 0), this.retryIds[e.requestId] += 1;
            if (!this.requestQueue.some(t => t.requestId === e.requestId)) {
              let t = setTimeout(() => {
                C(this.requestQueue) ? (this.requestQueue.push(e), this.initiateRequest()) : this.requestQueue.push(e), clearTimeout(t), t = null
              }, 800)
            }
          }, this.hoardingQueue = [], this.requestQueue = [], this.requestLimit = 3, this.requestTimeout = 5e3, this.retryLimit = 2, this.retryIds = {}, this.requestingNum = 0, this.requestURL = this.generateURL()
        }
      }
      class Oe {
        constructor(e) {
          var t;
          this.growingIO = e, this.initUserInfo = () => {
            var e;
            const {
              minipInstance: t
            } = this.growingIO, i = [this.uidStorageName, this.userIdStorageName, this.userKeyStorageName, this.gioIdStorageName], n = null !== (e = Q(t, i)) && void 0 !== e ? e : [];
            ["_uid", "_userId", "_userKey", "_gioId"].forEach((e, t) => {
              this[e] = n[t], "_uid" !== e || this[e] || (this.uid = q())
            })
          }, this.saveUserInfo = () => {
            const {
              minipInstance: e
            } = this.growingIO;
            J(e, [{
              key: this.uidStorageName,
              value: this.uid
            }, {
              key: this.userIdStorageName,
              value: this.userId
            }, {
              key: this.userKeyStorageName,
              value: this.userKey
            }, {
              key: this.gioIdStorageName,
              value: this.gioId
            }])
          };
          const {
            inPlugin: i
          } = this.growingIO;
          this.uidStorageName = i ? "_growing_plugin_uid_" : "_growing_uid_", this.userIdStorageName = i ? "_growing_plugin_userId_" : "_growing_userId_", this.userKeyStorageName = i ? "_growing_plugin_userKey_" : "_growing_userKey_", this.gioIdStorageName = i ? "_growing_plugin_gioId_" : "_growing_gioId_", this._sessionId = q(), this._uid = void 0, this._userId = void 0, this._userKey = void 0, this._gioId = void 0, "quickapp" !== (null === (t = this.growingIO) || void 0 === t ? void 0 : t.gioPlatform) && this.initUserInfo()
        }
        get sessionId() {
          return this._sessionId || (this._sessionId = q()), this._sessionId
        }
        set sessionId(e) {
          const t = this._sessionId;
          this._sessionId = e || q(), t !== this._sessionId && this.growingIO.emitter.emit("SESSIONID_UPDATE", {
            newSessionId: this._sessionId,
            oldSessionId: t
          })
        }
        get uid() {
          return this._uid
        }
        set uid(e) {
          const t = this._uid;
          this._uid = e, t !== this._uid && (this.growingIO.minipInstance.setStorage(this.uidStorageName, this._uid), this.growingIO.emitter.emit("UID_UPDATE", {
            newUId: e,
            oldUId: t
          }))
        }
        get userId() {
          return this._userId
        }
        set userId(e) {
          const t = this._userId;
          this._userId = e, t !== this._userId && (this.growingIO.minipInstance.setStorage(this.userIdStorageName, this._userId), this.growingIO.emitter.emit("USERID_UPDATE", {
            newUserId: e,
            oldUserId: t
          })), e && (this.gioId = e)
        }
        get userKey() {
          return this._userKey
        }
        set userKey(e) {
          const t = this._userKey;
          this._userKey = e, t !== this._userKey && (this.growingIO.minipInstance.setStorage(this.userKeyStorageName, this._userKey), this.growingIO.emitter.emit("USERKEY_UPDATE", {
            newUserKey: e,
            oldUserKey: t
          }))
        }
        get gioId() {
          return this._gioId
        }
        set gioId(e) {
          const t = this._gioId;
          this._gioId = e, t !== this._gioId && (this.growingIO.minipInstance.setStorage(this.gioIdStorageName, this._gioId), this.growingIO.emitter.emit("GIOID_UPDATE", {
            newGioId: e,
            oldGioId: t
          }))
        }
      }
      const Pe = new class {
          constructor() {
            var e;
            this.registerPlugins = e => {
              this.plugins.pluginItems = [...this.plugins.pluginItems, ...e], this.plugins.installAll(e)
            }, this.init = e => {
              var t;
              return A("Gio小程序SDK 初始化中...", "info"), this.dataStore.initOptions(e), null === (t = this.emitter) || void 0 === t || t.emit("OPTION_INITIALIZED", this), this.gioSDKInitialized = !0, this.vdsConfig.subpackage || (V().__gio__ = () => this), this.uploader = new Ce(this), this.vdsConfig.idMapping || (this.userStore.userKey = ""), this.emitter.emit("SDK_INITIALIZED", this), A("Gio小程序SDK 初始化完成！", "success"), this.vdsConfig.forceLogin && A("forceLogin已开启，请调用 identify 方法设置 openId 以继续上报!", "info"), this.inPlugin && "tbp" !== this.minipInstance.platform && this.dataStore.sendVisit(), !0
            }, this.getOption = e => this.dataStore.getOption(e), this.setOption = (e, t) => {
              if (k(ie).includes(e)) {
                const i = this.dataStore.setOption(e, t);
                return i && ie[e] && A("已".concat(t ? "开启" : "关闭").concat(ie[e]), "info"), i
              }
              return A("不存在可修改的配置项：".concat(e, "，请检查后重试!"), "warn"), !1
            }, this.getDeviceId = () => this.userStore.uid, this.identify = e => {
              if (this.vdsConfig.forceLogin) {
                if (!X(e)) return void E("identify");
                const t = f(e).slice(0, 1e3);
                this.userStore.uid = t, this.uploader.hoardingQueue.forEach((e, i) => this.uploader.hoardingQueue[i].deviceId = t), this.dataStore.setOption("forceLogin", !1), this.uploader.initiateRequest(!0)
              } else E("identify", !1, "forceLogin未开启")
            }, this.setUserId = (e, t) => {
              if (X(e)) {
                const i = this.userStore.gioId;
                if (e = f(e).slice(0, 1e3), t = f(t).slice(0, 1e3), this.userStore.userId = e, this.vdsConfig.idMapping && (this.userStore.userKey = n(t) ? "" : t), i && i !== e) {
                  this.userStore.sessionId = "";
                  const {
                    path: e,
                    query: t,
                    settedTitle: i
                  } = this.dataStore.eventHooks.currentPage;
                  this.dataStore.eventHooks.currentPage.title = i[e] || this.minipInstance.getPageTitle(this.minipInstance.getCurrentPage()), this.dataStore.sendVisit({
                    path: e,
                    query: t
                  })
                }
              } else E("setUserId")
            }, this.clearUserId = () => {
              this.userStore.userId = void 0, this.userStore.userKey = void 0
            }, this.setUserAttributes = e => {
              var t, i;
              !C(e) && a(e) ? null === (i = null === (t = this.plugins) || void 0 === t ? void 0 : t.gioCustomTracking) || void 0 === i || i.buildUserAttributesEvent(e) : E("setUserAttributes")
            }, this.track = (e, t) => {
              var i, n;
              ((null === (n = null === (i = this.plugins) || void 0 === i ? void 0 : i.gioCustomTracking) || void 0 === n ? void 0 : n.buildCustomEvent) || function () {})(e, Object.assign(Object.assign({}, this.dataStore.generalProps), a(t) && !C(t) ? t : {}))
            }, this.trackTimerStart = e => !!this.vdsConfig.dataCollect && D(e, () => {
              const t = q();
              return this.dataStore.trackTimers[t] = {
                eventName: e,
                leng: 0,
                start: +Date.now()
              }, t
            }), this.trackTimerPause = e => {
              if (e && this.dataStore.trackTimers[e]) {
                const t = this.dataStore.trackTimers[e];
                return t.start && (t.leng = t.leng + (+Date.now() - t.start)), t.start = 0, !0
              }
              return !1
            }, this.trackTimerResume = e => {
              if (e && this.dataStore.trackTimers[e]) {
                const t = this.dataStore.trackTimers[e];
                return 0 === t.start && (t.start = +Date.now()), !0
              }
              return !1
            }, this.trackTimerEnd = (e, t) => {
              if (this.vdsConfig.dataCollect) {
                const i = 864e5;
                if (e && this.dataStore.trackTimers[e]) {
                  const n = this.dataStore.trackTimers[e];
                  if (0 !== n.start) {
                    const e = +Date.now() - n.start;
                    n.leng = e > 0 ? n.leng + e : 0
                  }
                  const {
                    eventContextBuilder: o,
                    eventInterceptor: r
                  } = this.dataStore;
                  return r(Object.assign(Object.assign({
                    eventType: "CUSTOM",
                    eventName: n.eventName,
                    attributes: K(Object.assign(Object.assign({}, t), {
                      event_duration: n.leng > i ? 0 : n.leng / 1e3
                    }))
                  }, o()), {
                    customEventType: 0
                  })), this.removeTimer(e), !0
                }
                return A("未查找到对应的计时器，请检查!", "error"), !1
              }
              return !1
            }, this.removeTimer = e => !(!e || !this.dataStore.trackTimers[e] || (delete this.dataStore.trackTimers[e], 0)), this.clearTrackTimer = () => {
              this.dataStore.trackTimers = {}
            }, this.setGeneralProps = e => {
              a(e) && !C(e) ? (this.dataStore.generalProps = Object.assign(Object.assign({}, this.dataStore.generalProps), e), k(this.dataStore.generalProps).forEach(e => {
                [void 0, null].includes(this.dataStore.generalProps[e]) && (this.dataStore.generalProps[e] = "")
              })) : E("setGeneralProps")
            }, this.clearGeneralProps = e => {
              l(e) && !C(e) ? e.forEach(e => {
                T(this.dataStore.generalProps, e)
              }) : this.dataStore.generalProps = {}
            }, this.setPageAttributes = e => {
              const {
                currentPage: t
              } = this.dataStore.eventHooks, i = this.minipInstance.getCurrentPath();
              ["onLoad", "attached"].includes(t.currentLifecycle) && (t.pageProps[i] = K(e))
            }, this.updateImpression = () => {
              A("当前未集成半自动浏览插件，请集成插件后再调用 updateImpression!", "warn")
            }, this.setLocation = (e, t) => {
              const i = {
                  latitude: e,
                  longitude: t
                },
                n = this.dataStore.locationData,
                o = e => e >= -180 && 180 >= e;
              o(e) && o(t) && (n.latitude !== e || n.longitude !== t) && (this.dataStore.locationData = i)
            }, this.getGioInfo = () => {
              const {
                uid: e,
                userId: t,
                userKey: i,
                sessionId: n
              } = this.userStore, {
                projectId: o,
                appId: r,
                dataSourceId: s,
                dataCollect: a,
                idMapping: c,
                extraParams: l,
                ignoreFields: u
              } = this.vdsConfig, h = {
                gioappid: r,
                giocs1: t || "",
                gioplatform: this.platformConfig.platform,
                gioprojectid: o,
                gios: n,
                giou: e
              };
              return h.giodatacollect = a, h.giodatasourceid = s, c && (h.giouserkey = i), C(l) || l.forEach(e => {
                u.includes(e) || (h["gio" + e] = this.dataStore.lastVisitEvent[e])
              }), xe.stringify(h)
            }, this.utils = Object.assign(Object.assign(Object.assign({}, P), Z), {
              qs: xe
            }), this.emitter = {
              all: e = e || new Map,
              on: function (t, i) {
                var n = e.get(t);
                n ? n.push(i) : e.set(t, [i])
              },
              off: function (t, i) {
                var n = e.get(t);
                n && (i ? n.splice(n.indexOf(i) >>> 0, 1) : e.set(t, []))
              },
              emit: function (t, i) {
                var n = e.get(t);
                n && n.slice().map(function (e) {
                  e(i)
                }), (n = e.get("*")) && n.slice().map(function (e) {
                  e(t, i)
                })
              }
            }, this.gioPlatform = "wx", this.gioFramework = "native", this.sdkVersion = "4.0.0";
            try {
              "quickapp" === this.gioPlatform || c(getApp) && c(App) ? this.inPlugin = !1 : this.inPlugin = !0
            } catch (e) {
              this.inPlugin = !0
            }
            this.inPlugin && A("未检测到小程序实例，自动切换为插件模式!", "info"), this.platformConfig = ge, this.minipInstance = new me(this), this.dataStore = new pe(this), this.userStore = new Oe(this), this.plugins = new Se(this), this.plugins.innerPluginInit()
          }
        },
        Ae = function () {
          const e = arguments[0];
          if (o(e) && te.includes(e) && Pe[e]) {
            const i = p(Array.from(arguments));
            if ("init" === e) {
              const e = !(t = Pe).vdsConfig && !t.gioSDKInitialized || (A("SDK重复初始化，请检查是否重复加载SDK或接入其他平台SDK导致冲突!", "warn"), !1),
                n = !!d(i) || (A('SDK初始化失败，请使用 gdp("init", "您的GrowingIO项目 accountId", "您项目的 dataSourceId", "你的应用 AppId", options); 进行初始化!', "error"), !1),
                r = (e => {
                  const t = e[0];
                  let i = h(e);
                  return X(t) ? (a(i) && i || (i = {}), {
                    projectId: t,
                    userOptions: i
                  }) : (A("SDK初始化失败，accountId 参数不合法!", "error"), !1)
                })(i),
                s = (e => {
                  const t = e[1];
                  let i = e[2];
                  const n = h(e);
                  return t && o(t) ? X(i) ? {
                    dataSourceId: t,
                    appId: i,
                    options: n
                  } : (A("SDK初始化失败，appId 参数不合法!", "error"), !1) : (A("SDK初始化失败，dataSourceId 参数不合法!", "error"), !1)
                })(i);
              if (e && n && r && s) {
                const {
                  projectId: e
                } = r, {
                  dataSourceId: t,
                  appId: i,
                  options: n
                } = s;
                return Pe.init(Object.assign(Object.assign({}, n), {
                  projectId: e,
                  dataSourceId: t,
                  appId: i
                }))
              }
            } else if ("registerPlugins" === e) Pe.registerPlugins(i[0]);
            else {
              if (Pe.gioSDKInitialized && Pe.vdsConfig) return Pe[e](...i);
              A("SDK未初始化!", "error")
            }
          } else ne.includes(e) ? A("方法 ".concat(f(e), " 已被弃用!"), "warn") : A("不存在名为 ".concat(f(e), " 的方法调用!"), "error");
          var t
        };
      z().gdp = Ae, z().gioSDKVersion = Pe.sdkVersion;
      R(() => {
        var e;
        return null !== (e = Pe.dataStore.eventHooks.growingApp) && void 0 !== e ? e : App
      }), R(() => {
        var e;
        return null !== (e = Pe.dataStore.eventHooks.growingPage) && void 0 !== e ? e : Page
      }), R(() => {
        var e;
        return null !== (e = Pe.dataStore.eventHooks.growingComponent) && void 0 !== e ? e : Component
      }), R(() => {
        var e;
        return null !== (e = Pe.dataStore.eventHooks.growingBehavior) && void 0 !== e ? e : Behavior
      });
      var Ee = i(39),
        Re = i(124),
        Ne = {
          init: function () {
            const e = (0, Re.g)();
            let t, i;
            (0, Ee.bb)() && (t = "efe93414bc7be0e5", i = "8c54ac3cbb48a548"), Ae("init", t, i, e.appid, {
              version: e.appVersion,
              usePlugin: !0,
              forceLogin: !0,
              debug: !0
            })
          },
          gio: Ae
        }
    },
    187: function (e) {
      var t, i = Object.defineProperty,
        n = Object.defineProperties,
        o = Object.getOwnPropertyDescriptors,
        r = Object.getOwnPropertySymbols,
        s = Object.prototype.hasOwnProperty,
        a = Object.prototype.propertyIsEnumerable,
        c = (e, t, n) => t in e ? i(e, t, {
          enumerable: !0,
          configurable: !0,
          writable: !0,
          value: n
        }) : e[t] = n,
        l = (e, t) => {
          for (var i in t || (t = {})) s.call(t, i) && c(e, i, t[i]);
          if (r)
            for (var i of r(t)) a.call(t, i) && c(e, i, t[i]);
          return e
        },
        u = (e, t) => n(e, o(t));
      t = () => {
        var e = function (t, i) {
          return (e = Object.setPrototypeOf || {
              __proto__: []
            }
            instanceof Array && function (e, t) {
              e.__proto__ = t
            } || function (e, t) {
              for (const i in t) t.hasOwnProperty(i) && (e[i] = t[i])
            })(t, i)
        };

        function t(t, i) {
          function n() {
            this.constructor = t
          }
          e(t, i), t.prototype = null === i ? Object.create(i) : (n.prototype = i.prototype, new n)
        }

        function i(e, t, i, n) {
          let o;
          const r = arguments.length;
          let s = r < 3 ? t : null === n ? n = Object.getOwnPropertyDescriptor(t, i) : n;
          if ("object" == typeof Reflect && "function" == typeof Reflect.decorate) s = Reflect.decorate(e, t, i, n);
          else
            for (let n = e.length - 1; n >= 0; n--)(o = e[n]) && (s = (r < 3 ? o(s) : r > 3 ? o(t, i, s) : o(t, i)) || s);
          return r > 3 && s && Object.defineProperty(t, i, s), s
        }

        function n() {
          for (var e = 0, t = 0, i = arguments.length; t < i; t++) e += arguments[t].length;
          const n = Array(e);
          let o = 0;
          for (t = 0; t < i; t++)
            for (let e = arguments[t], i = 0, r = e.length; i < r; i++, o++) n[o] = e[i];
          return n
        }
        try {
          Object.entries || (Object.entries = function (e) {
            for (var t = Object.keys(e), i = t.length, n = new Array(i); i--;) n[i] = [t[i], e[t[i]]];
            return n
          }), Array.prototype.includes || (Array.prototype.includes = function (e) {
            return !!~this.indexOf(e)
          })
        } catch (e) {
          console.error("polyfill exec failed", e)
        }
        let o, r;
        const s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
          a = /^(?:[A-Za-z\d+\/]{4})*?(?:[A-Za-z\d+\/]{2}(?:==)?|[A-Za-z\d+\/]{3}=?)?$/,
          c = function (e) {
            for (var t, i, n, o, r = "", a = 0, c = (e = String(e)).length % 3; a < e.length;) {
              if ((i = e.charCodeAt(a++)) > 255 || (n = e.charCodeAt(a++)) > 255 || (o = e.charCodeAt(a++)) > 255) throw new TypeError("Failed to execute 'btoa' on 'Window': The string to be encoded contains characters outside of the Latin1 range.");
              r += s.charAt((t = i << 16 | n << 8 | o) >> 18 & 63) + s.charAt(t >> 12 & 63) + s.charAt(t >> 6 & 63) + s.charAt(63 & t)
            }
            return c ? r.slice(0, c - 3) + "===".substring(c) : r
          },
          h = {
            uint8ArrayToBase64(e) {
              for (var t = [], i = 0, n = e.length; i < n; i += 4096) t.push(String.fromCharCode.apply(null, e.subarray(i, i + 4096)));
              return c(t.join(""))
            },
            encode(e) {
              return (t = e, c(encodeURIComponent(t).replace(/%([0-9A-F]{2})/g, (e, t) => {
                let i;
                return i = "0x".concat(t), String.fromCharCode(i)
              }))).replace(/=/g, "").replace(/\+/g, "-").replace(/\//g, "_");
              var t
            },
            decode(e) {
              const t = (e = e.replace(/\-/g, "+").replace(/_/g, "/")).length % 4;
              return t > 0 && (e += "====".substring(t)),
                function (e) {
                  return decodeURIComponent(function (e) {
                    if (e = String(e).replace(/[\t\n\f\r ]+/g, ""), !a.test(e)) throw new TypeError("Failed to execute 'atob' on 'Window': The string to be decoded is not correctly encoded.");
                    e += "==".slice(2 - (3 & e.length));
                    for (var t, i, n, o = "", r = 0; r < e.length;) t = s.indexOf(e.charAt(r++)) << 18 | s.indexOf(e.charAt(r++)) << 12 | (i = s.indexOf(e.charAt(r++))) << 6 | (n = s.indexOf(e.charAt(r++))), o += 64 === i ? String.fromCharCode(t >> 16 & 255) : 64 === n ? String.fromCharCode(t >> 16 & 255, t >> 8 & 255) : String.fromCharCode(t >> 16 & 255, t >> 8 & 255, 255 & t);
                    return o
                  }(e).split("").map(e => "%".concat("00".concat(e.charCodeAt(0).toString(16)).slice(-2))).join(""))
                }(e)
            }
          },
          p = Object.prototype.toString,
          d = h,
          g = function (e) {
            return "[object Object]" === p.call(e)
          },
          f = function (e) {
            return "[object Array]" === p.call(e)
          },
          m = function (e, t) {
            let i;
            void 0 === t && (t = 0);
            let n = [];
            return function () {
              for (var o = arguments, r = [], s = 0; s < arguments.length; s++) r[s] = o[s];
              return clearTimeout(i), i = setTimeout(() => {
                const t = e.apply(void 0, r);
                n.forEach(e => e(t)), n = []
              }, t), new Promise(e => n.push(e))
            }
          },
          y = function () {
            return "".concat(Date.now(), "-").concat("xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, e => {
              const t = 16 * Math.random() | 0;
              return ("x" == e ? t : 3 & t | 8).toString(16)
            }))
          };
        var v = function () {
          for (var e = arguments, t = [], i = 0; i < arguments.length; i++) t[i] = e[i];
          return 0 === t.length ? {} : t.length < 2 ? t[0] : t.reduce((e, t) => {
            if (!g(e) || !g(t)) return console.error("deepMerge arguments only access object"), e;
            const i = e || {};
            return Object.entries(t).forEach(t => {
              const o = t[0],
                r = t[1];
              if (void 0 !== r)
                if (e[o])
                  if (f(e[o])) {
                    if (!f(r)) return void(i[o] = r);
                    const t = f(r) ? r : [r];
                    i[o] = n(e[o], t)
                  } else g(e[o]) ? i[o] = v(e[o], r) : i[o] = r;
              else i[o] = r
            }), i
          })
        };
        const _ = function (e) {
            return !!/^[a-zA-Z\$_][a-zA-Z\d_]*$/.test(e)
          },
          b = /^v?(?:\d+)(\.(?:[x*]|\d+)(\.(?:[x*]|\d+)(\.(?:[x*]|\d+))?(?:-[\da-z\-]+(?:\.[\da-z\-]+)*)?(?:\+[\da-z\-]+(?:\.[\da-z\-]+)*)?)?)?$/i,
          k = function (e) {
            if ("string" != typeof e) throw new TypeError("Invalid argument expected string");
            if (!b.test(e)) throw new Error("Invalid argument not valid semver ('".concat(e, "' received)"))
          },
          S = function (e) {
            return isNaN(Number(e)) ? e : Number(e)
          },
          x = function (e) {
            let t, i;
            const n = e.replace(/^v/, "").replace(/\+.*$/, ""),
              o = (i = "-", -1 === (t = n).indexOf("-") ? t.length : t.indexOf("-")),
              r = n.substring(0, o).split(".");
            return r.push(n.substring(o + 1)), r
          },
          w = function (e, t) {
            [e, t].forEach(k);
            for (var i = x(e), n = x(t), o = 0; o < Math.max(i.length - 1, n.length - 1); o++) {
              const e = parseInt(i[o] || 0, 10),
                t = parseInt(n[o] || 0, 10);
              if (e > t) return 1;
              if (t > e) return -1
            }
            const r = i[i.length - 1],
              s = n[n.length - 1];
            if (r && s) {
              const e = r.split(".").map(S),
                t = s.split(".").map(S);
              for (o = 0; o < Math.max(e.length, t.length); o++) {
                if (void 0 === e[o] || "string" == typeof t[o] && "number" == typeof e[o]) return -1;
                if (void 0 === t[o] || "string" == typeof e[o] && "number" == typeof t[o]) return 1;
                if (e[o] > t[o]) return 1;
                if (t[o] > e[o]) return -1
              }
            } else if (r || s) return r ? -1 : 1;
            return 0
          },
          T = function (e) {
            if ("string" == typeof e) return e;
            try {
              return (JSON.stringify(e, (e2 = [], r2 = [], function (e, t) {
                if (t instanceof Error) return "Error.message: ".concat(t.message, " \n  Error.stack: ").concat(t.stack);
                if ("object" == typeof t && null !== t) {
                  const i = e2.indexOf(t);
                  if (-1 !== i) return "[Circular ".concat(r2[i], "]");
                  e2.push(t), r2.push(e || "root")
                }
                return t
              }), 4) || "undefined").replace(/"/gim, "")
            } catch (e) {
              return "error happen when sdk stringify: \n ".concat(e.message, " \n ").concat(e.stack)
            }
          },
          I = function () {
            return "undefined" != typeof jd ? jd : "undefined" != typeof tt ? tt : "undefined" != typeof qq ? qq : "undefined" != typeof swan ? swan : "undefined" != typeof dd ? dd : "undefined" != typeof my ? my : wx
          },
          C = function () {
            return "undefined" != typeof dd ? dd.httpRequest : I().request
          },
          O = function (e) {
            function i(t) {
              const i = e.call(this, t.request) || this;
              return i.stack = [], i.initialize = function () {
                return Promise.resolve(!0)
              }, i.add = function (e) {
                i.stack.push(e)
              }, i.getItems = function () {
                return i.stack
              }, i.unshift = function (e) {
                let t;
                return (t = i.stack).unshift.apply(t, e)
              }, i.clean = function () {
                const e = i.stack;
                return i.stack = [], e
              }, i.checkQueue = function () {
                i.stack.length > 100 && (i.stack = i.stack.slice(-100))
              }, i.option = t, i.initialize(), i
            }
            return t(i, e), i.prototype.flush = function (e, t) {
              const i = this;
              if (void 0 === e && (e = {}), this.stack.length) {
                const o = JSON.parse(JSON.stringify(e));
                o.idenTifier += t;
                const r = this.stack.map(e => (e.props = l(l({}, e.props), o), e));
                this.stack = [], this.request({
                  events: r
                }).then(e => {
                  e.success || (i.stack = n(i.stack, r))
                }).catch(() => {
                  i.stack = n(i.stack, r)
                })
              }
            }, i
          }(function (e) {
            this.delay = 100, this.upload = m(e, this.delay), this.request = e
          }),
          P = "__SR_SDK_TRACKER__",
          A = "TRACKS",
          E = "USER_INFO",
          R = "LOGID_EVENTS",
          N = "IDENTIFIERUSER",
          D = "REPORTING",
          q = "PAUSED",
          M = "should exec cacheManagerInitialize first",
          U = "SDK_INTERNAL_ERROR",
          j = ["page", "page_title", "time", "chan_wxapp_scene", "chan_id", "chan_refer_app_id", "room_id"],
          F = ["app_id", "open_id", "user_id", "union_id", "local_id"],
          L = I(),
          G = [],
          B = L.request,
          H = function (e) {
            return G.forEach(t => {
              let i;
              try {
                e.requestStartTime = Date.now(), null === (i = t.onStart) || void 0 === i || i.call(t, e)
              } catch (e) {}
            }), B(u(l({}, e), {
              success(t) {
                let i;
                G.forEach(i => {
                  let n;
                  try {
                    null === (n = i.success) || void 0 === n || n.call(i, t, e)
                  } catch (e) {
                    try {
                      o("sdk_error_log", {
                        _sdk_error_log: {
                          message: "request success error",
                          type: U,
                          error: e.message
                        }
                      })
                    } catch (e) {}
                  }
                }), null === (i = e.success) || void 0 === i || i.call(e, t)
              },
              fail(t) {
                let i;
                G.forEach(i => {
                  let n;
                  try {
                    null === (n = i.fail) || void 0 === n || n.call(i, t, e)
                  } catch (e) {
                    try {
                      o("sdk_error_log", {
                        _sdk_error_log: {
                          message: "request fail error",
                          type: U,
                          error: e.message
                        }
                      })
                    } catch (e) {}
                  }
                }), null === (i = e.fail) || void 0 === i || i.call(e, t)
              },
              complete(t) {
                let i;
                G.forEach(i => {
                  let n;
                  try {
                    null === (n = i.complete) || void 0 === n || n.call(i, t, e)
                  } catch (e) {
                    try {
                      o("sdk_error_log", {
                        _sdk_error_log: {
                          message: "request complete error",
                          type: U,
                          error: e.message
                        }
                      })
                    } catch (e) {}
                  }
                }), null === (i = e.complete) || void 0 === i || i.call(e, t)
              }
            }))
          };
        let W = !1;
        const V = function (e, t) {
            o || (o = t), !W && function () {
              try {
                Object.defineProperty(L, "request", {
                  get() {
                    return H
                  }
                })
              } catch (e) {
                console.warn("cannot override `request`, error is: ", e)
              } finally {
                W = !0
              }
            }(), G.push(e)
          },
          z = I(),
          K = I(),
          Q = [],
          J = K.requestPayment,
          $ = K.requestOrderPayment,
          Y = function (e, t) {
            let i = J;
            return "requestOrderPayment" == t && (i = $), Q.forEach(t => {
              let i;
              try {
                null === (i = t.onStart) || void 0 === i || i.call(t, e)
              } catch (e) {
                try {
                  r("sdk_error_log", {
                    _sdk_error_log: {
                      message: "requestPayment onStart error",
                      type: U,
                      error: e.message
                    }
                  })
                } catch (e) {}
              }
            }), i(u(l({}, e), {
              success(t) {
                let i;
                Q.forEach(i => {
                  let n;
                  try {
                    null === (n = i.success) || void 0 === n || n.call(i, t, e)
                  } catch (e) {
                    try {
                      r("sdk_error_log", {
                        _sdk_error_log: {
                          message: "requestPayment success error",
                          type: U,
                          error: e.message
                        }
                      })
                    } catch (e) {}
                  }
                }), null === (i = e.success) || void 0 === i || i.call(e, t)
              },
              fail(t) {
                let i;
                Q.forEach(i => {
                  let n;
                  try {
                    null === (n = i.fail) || void 0 === n || n.call(i, t, e)
                  } catch (e) {
                    try {
                      r("sdk_error_log", {
                        _sdk_error_log: {
                          message: "requestPayment fail error",
                          type: U,
                          error: e.message
                        }
                      })
                    } catch (e) {}
                  }
                }), null === (i = e.fail) || void 0 === i || i.call(e, t)
              }
            }))
          };
        let Z = !1;
        const X = function (e, t, i) {
            const n = i.value;
            return i.value = function () {
              let e;
              try {
                e = n.apply(this, arguments)
              } catch (e) {
                try {
                  console.error("Calling ".concat(t, " error with"), arguments), console.error(e);
                  const i = this.getServerUrl();
                  this.request({
                    type: "sdk api exec error",
                    props: {
                      sr_sdk_version: this.version,
                      system_info: this.getSystemInfo(),
                      framework_info: this.getFrameworkInfo(),
                      message: (e || {}).message || e,
                      stack: (e || {}).stack
                    }
                  }, {
                    url: i,
                    method: "POST"
                  })
                } catch (e) {}
              }
              return e
            }, i
          },
          ee = function (e, t, i) {
            const n = i.value;
            return i.value = function () {
              if (this.inited) return n.apply(this, arguments);
              console.error("请先完成初始化")
            }, i
          },
          te = function () {
            function e() {}
            return e.AddUnsigned = function (e, t) {
              let i, n, o, r, s;
              return o = 2147483648 & e, r = 2147483648 & t, s = (1073741823 & e) + (1073741823 & t), (i = 1073741824 & e) & (n = 1073741824 & t) ? 2147483648 ^ s ^ o ^ r : i | n ? 1073741824 & s ? 3221225472 ^ s ^ o ^ r : 1073741824 ^ s ^ o ^ r : s ^ o ^ r
            }, e.FF = function (e, t, i, n, o, r, s) {
              return e = this.AddUnsigned(e, this.AddUnsigned(this.AddUnsigned(this.F(t, i, n), o), s)), this.AddUnsigned(this.RotateLeft(e, r), t)
            }, e.GG = function (e, t, i, n, o, r, s) {
              return e = this.AddUnsigned(e, this.AddUnsigned(this.AddUnsigned(this.G(t, i, n), o), s)), this.AddUnsigned(this.RotateLeft(e, r), t)
            }, e.HH = function (e, t, i, n, o, r, s) {
              return e = this.AddUnsigned(e, this.AddUnsigned(this.AddUnsigned(this.H(t, i, n), o), s)), this.AddUnsigned(this.RotateLeft(e, r), t)
            }, e.II = function (e, t, i, n, o, r, s) {
              return e = this.AddUnsigned(e, this.AddUnsigned(this.AddUnsigned(this.I(t, i, n), o), s)), this.AddUnsigned(this.RotateLeft(e, r), t)
            }, e.ConvertToWordArray = function (e) {
              for (var t, i = e.length, n = i + 8, o = 16 * ((n - n % 64) / 64 + 1), r = Array(o - 1), s = 0, a = 0; a < i;) s = a % 4 * 8, r[t = (a - a % 4) / 4] = r[t] | e.charCodeAt(a) << s, a++;
              return s = a % 4 * 8, r[t = (a - a % 4) / 4] = r[t] | 128 << s, r[o - 2] = i << 3, r[o - 1] = i >>> 29, r
            }, e.WordToHex = function (e) {
              let t, i = "",
                n = "";
              for (t = 0; t <= 3; t++) i += (n = "0".concat((e >>> 8 * t & 255).toString(16))).substr(n.length - 2, 2);
              return i
            }, e.Utf8Encode = function (e) {
              let t, i = "";
              e = e.replace(/\r\n/g, "\n");
              for (let n = 0; n < e.length; n++)(t = e.charCodeAt(n)) < 128 ? i += String.fromCharCode(t) : t > 127 && t < 2048 ? (i += String.fromCharCode(t >> 6 | 192), i += String.fromCharCode(63 & t | 128)) : (i += String.fromCharCode(t >> 12 | 224), i += String.fromCharCode(t >> 6 & 63 | 128), i += String.fromCharCode(63 & t | 128));
              return i
            }, e.init = function (e) {
              for ("string" != typeof e && (e = JSON.stringify(e)), this._string = this.Utf8Encode(e), this.x = this.ConvertToWordArray(this._string), this.a = 1732584193, this.b = 4023233417, this.c = 2562383102, this.d = 271733878, this.k = 0; this.k < this.x.length; this.k += 16) this.AA = this.a, this.BB = this.b, this.CC = this.c, this.DD = this.d, this.a = this.FF(this.a, this.b, this.c, this.d, this.x[this.k], this.S11, 3614090360), this.d = this.FF(this.d, this.a, this.b, this.c, this.x[this.k + 1], this.S12, 3905402710), this.c = this.FF(this.c, this.d, this.a, this.b, this.x[this.k + 2], this.S13, 606105819), this.b = this.FF(this.b, this.c, this.d, this.a, this.x[this.k + 3], this.S14, 3250441966), this.a = this.FF(this.a, this.b, this.c, this.d, this.x[this.k + 4], this.S11, 4118548399), this.d = this.FF(this.d, this.a, this.b, this.c, this.x[this.k + 5], this.S12, 1200080426), this.c = this.FF(this.c, this.d, this.a, this.b, this.x[this.k + 6], this.S13, 2821735955), this.b = this.FF(this.b, this.c, this.d, this.a, this.x[this.k + 7], this.S14, 4249261313), this.a = this.FF(this.a, this.b, this.c, this.d, this.x[this.k + 8], this.S11, 1770035416), this.d = this.FF(this.d, this.a, this.b, this.c, this.x[this.k + 9], this.S12, 2336552879), this.c = this.FF(this.c, this.d, this.a, this.b, this.x[this.k + 10], this.S13, 4294925233), this.b = this.FF(this.b, this.c, this.d, this.a, this.x[this.k + 11], this.S14, 2304563134), this.a = this.FF(this.a, this.b, this.c, this.d, this.x[this.k + 12], this.S11, 1804603682), this.d = this.FF(this.d, this.a, this.b, this.c, this.x[this.k + 13], this.S12, 4254626195), this.c = this.FF(this.c, this.d, this.a, this.b, this.x[this.k + 14], this.S13, 2792965006), this.b = this.FF(this.b, this.c, this.d, this.a, this.x[this.k + 15], this.S14, 1236535329), this.a = this.GG(this.a, this.b, this.c, this.d, this.x[this.k + 1], this.S21, 4129170786), this.d = this.GG(this.d, this.a, this.b, this.c, this.x[this.k + 6], this.S22, 3225465664), this.c = this.GG(this.c, this.d, this.a, this.b, this.x[this.k + 11], this.S23, 643717713), this.b = this.GG(this.b, this.c, this.d, this.a, this.x[this.k], this.S24, 3921069994), this.a = this.GG(this.a, this.b, this.c, this.d, this.x[this.k + 5], this.S21, 3593408605), this.d = this.GG(this.d, this.a, this.b, this.c, this.x[this.k + 10], this.S22, 38016083), this.c = this.GG(this.c, this.d, this.a, this.b, this.x[this.k + 15], this.S23, 3634488961), this.b = this.GG(this.b, this.c, this.d, this.a, this.x[this.k + 4], this.S24, 3889429448), this.a = this.GG(this.a, this.b, this.c, this.d, this.x[this.k + 9], this.S21, 568446438), this.d = this.GG(this.d, this.a, this.b, this.c, this.x[this.k + 14], this.S22, 3275163606), this.c = this.GG(this.c, this.d, this.a, this.b, this.x[this.k + 3], this.S23, 4107603335), this.b = this.GG(this.b, this.c, this.d, this.a, this.x[this.k + 8], this.S24, 1163531501), this.a = this.GG(this.a, this.b, this.c, this.d, this.x[this.k + 13], this.S21, 2850285829), this.d = this.GG(this.d, this.a, this.b, this.c, this.x[this.k + 2], this.S22, 4243563512), this.c = this.GG(this.c, this.d, this.a, this.b, this.x[this.k + 7], this.S23, 1735328473), this.b = this.GG(this.b, this.c, this.d, this.a, this.x[this.k + 12], this.S24, 2368359562), this.a = this.HH(this.a, this.b, this.c, this.d, this.x[this.k + 5], this.S31, 4294588738), this.d = this.HH(this.d, this.a, this.b, this.c, this.x[this.k + 8], this.S32, 2272392833), this.c = this.HH(this.c, this.d, this.a, this.b, this.x[this.k + 11], this.S33, 1839030562), this.b = this.HH(this.b, this.c, this.d, this.a, this.x[this.k + 14], this.S34, 4259657740), this.a = this.HH(this.a, this.b, this.c, this.d, this.x[this.k + 1], this.S31, 2763975236), this.d = this.HH(this.d, this.a, this.b, this.c, this.x[this.k + 4], this.S32, 1272893353), this.c = this.HH(this.c, this.d, this.a, this.b, this.x[this.k + 7], this.S33, 4139469664), this.b = this.HH(this.b, this.c, this.d, this.a, this.x[this.k + 10], this.S34, 3200236656), this.a = this.HH(this.a, this.b, this.c, this.d, this.x[this.k + 13], this.S31, 681279174), this.d = this.HH(this.d, this.a, this.b, this.c, this.x[this.k], this.S32, 3936430074), this.c = this.HH(this.c, this.d, this.a, this.b, this.x[this.k + 3], this.S33, 3572445317), this.b = this.HH(this.b, this.c, this.d, this.a, this.x[this.k + 6], this.S34, 76029189), this.a = this.HH(this.a, this.b, this.c, this.d, this.x[this.k + 9], this.S31, 3654602809), this.d = this.HH(this.d, this.a, this.b, this.c, this.x[this.k + 12], this.S32, 3873151461), this.c = this.HH(this.c, this.d, this.a, this.b, this.x[this.k + 15], this.S33, 530742520), this.b = this.HH(this.b, this.c, this.d, this.a, this.x[this.k + 2], this.S34, 3299628645), this.a = this.II(this.a, this.b, this.c, this.d, this.x[this.k], this.S41, 4096336452), this.d = this.II(this.d, this.a, this.b, this.c, this.x[this.k + 7], this.S42, 1126891415), this.c = this.II(this.c, this.d, this.a, this.b, this.x[this.k + 14], this.S43, 2878612391), this.b = this.II(this.b, this.c, this.d, this.a, this.x[this.k + 5], this.S44, 4237533241), this.a = this.II(this.a, this.b, this.c, this.d, this.x[this.k + 12], this.S41, 1700485571), this.d = this.II(this.d, this.a, this.b, this.c, this.x[this.k + 3], this.S42, 2399980690), this.c = this.II(this.c, this.d, this.a, this.b, this.x[this.k + 10], this.S43, 4293915773), this.b = this.II(this.b, this.c, this.d, this.a, this.x[this.k + 1], this.S44, 2240044497), this.a = this.II(this.a, this.b, this.c, this.d, this.x[this.k + 8], this.S41, 1873313359), this.d = this.II(this.d, this.a, this.b, this.c, this.x[this.k + 15], this.S42, 4264355552), this.c = this.II(this.c, this.d, this.a, this.b, this.x[this.k + 6], this.S43, 2734768916), this.b = this.II(this.b, this.c, this.d, this.a, this.x[this.k + 13], this.S44, 1309151649), this.a = this.II(this.a, this.b, this.c, this.d, this.x[this.k + 4], this.S41, 4149444226), this.d = this.II(this.d, this.a, this.b, this.c, this.x[this.k + 11], this.S42, 3174756917), this.c = this.II(this.c, this.d, this.a, this.b, this.x[this.k + 2], this.S43, 718787259), this.b = this.II(this.b, this.c, this.d, this.a, this.x[this.k + 9], this.S44, 3951481745), this.a = this.AddUnsigned(this.a, this.AA), this.b = this.AddUnsigned(this.b, this.BB), this.c = this.AddUnsigned(this.c, this.CC), this.d = this.AddUnsigned(this.d, this.DD);
              return (this.WordToHex(this.a) + this.WordToHex(this.b) + this.WordToHex(this.c) + this.WordToHex(this.d)).toLowerCase()
            }, e.x = [], e.S11 = 7, e.S12 = 12, e.S13 = 17, e.S14 = 22, e.S21 = 5, e.S22 = 9, e.S23 = 14, e.S24 = 20, e.S31 = 4, e.S32 = 11, e.S33 = 16, e.S34 = 23, e.S41 = 6, e.S42 = 10, e.S43 = 15, e.S44 = 21, e.RotateLeft = function (e, t) {
              return e << t | e >>> 32 - t
            }, e.F = function (e, t, i) {
              return e & t | ~e & i
            }, e.G = function (e, t, i) {
              return e & i | t & ~i
            }, e.H = function (e, t, i) {
              return e ^ t ^ i
            }, e.I = function (e, t, i) {
              return t ^ (e | ~i)
            }, e
          }(),
          ie = I();

        function ne() {
          const e = getCurrentPages() || "";
          return e[e.length - 1] || ""
        }

        function oe(e) {
          let t = "/";
          try {
            const i = ne();
            if (!i) return i;
            let n;
            const o = i.route || i.__route__,
              r = i.options || {};
            for (const s in n = i.options || {}, t = "".concat(o, "?"), r) "share" === e && "txsrShareInfoSdk" === s || _(s) && n[s] && (t += "".concat(s, "=").concat(r[s], "&"));
            t = t.substring(0, t.length - 1)
          } catch (e) {
            console.error("getCurrentPageUrlWithArgs error", e)
          }
          return t
        }

        function re(e) {
          try {
            const t = ne();
            if (!t) return t;
            return t.options, (t.options || {})[e] || ""
          } catch (e) {
            console.error("getCurrentPageKey error", e)
          }
          return "/"
        }

        function se() {
          try {
            return ("undefined" != typeof tt ? function () {
              let e;
              const t = ne();
              try {
                const i = t.route || t.__route__;
                let n = "";
                return n = "undefined" != typeof __ttConfig ? __ttConfig.global.window.navigationBarTitleText : TMAConfig.global.window.navigationBarTitleText, (t ? null === (e = __allConfig__[i]) || void 0 === e ? void 0 : e.navigationBarTitleText : "") || n
              } catch (e) {}
            }() : "undefined" != typeof jd ? function () {
              let e, t;
              const i = ne();
              try {
                const n = __jdConfig.global.window.navigationBarTitleText;
                return (i ? ((null === (t = null === (e = __jdConfig.page) || void 0 === e ? void 0 : e["".concat(i.route, ".html")]) || void 0 === t ? void 0 : t.window) || {}).navigationBarTitleText : "") || n
              } catch (e) {}
            }() : function () {
              let e, t, i;
              const n = ne();
              try {
                const o = __wxConfig.global.window.navigationBarTitleText,
                  r = n ? ((null === (t = null === (e = __wxConfig.page) || void 0 === e ? void 0 : e["".concat(n.route, ".html")]) || void 0 === t ? void 0 : t.window) || {}).navigationBarTitleText : "",
                  s = null === (i = null === __wxAppCode__ || void 0 === __wxAppCode__ ? void 0 : __wxAppCode__["".concat(n.route, ".json")]) || void 0 === i ? void 0 : i.navigationBarTitleText;
                return r || s || o
              } catch (e) {}
            }()) || "未知"
          } catch (e) {}
          return "未知"
        }

        function ae(e, t, i) {
          try {
            const c = e[0],
              u = void 0 === c ? {} : c;
            if (u) switch (u.type) {
              case "tap":
              case "longpress":
              case "longtap":
              case "confirm":
                var n = (u.currentTarget || {}).dataset,
                  o = void 0 === n ? {} : n;
                0 == Object.keys(o).length && (o = u.target.dataset);
                var r = this || {},
                  s = r.is,
                  a = void 0 === s ? "" : s;
                r.data, t("element", l({
                  is_sdk_auto_track: !0,
                  is: a,
                  type: u.type,
                  element_id: "#".concat(i)
                }, o))
            }
          } catch (e) {
            console.error("elementEventTrack error", e)
          }
        }

        function ce() {
          let e;
          const t = (ne() || {}).route || "";
          try {
            e = ie.getStorageSync("".concat(P, "_production"))
          } catch (e) {
            console.error("CacheManager.get error", e)
          }
          const i = e.USER_INFO || {},
            n = i.local_id,
            o = i.txsr_from_share_info,
            r = void 0 === o ? {} : o,
            s = r.mi;
          let a = void 0 === s ? "" : s;
          const c = r.d,
            l = void 0 === c ? 0 : c,
            u = r.o;
          let h = void 0 === u ? "" : u;
          const p = te.init(n + t),
            d = "" !== a && p === a ? l : l + 1;
          return a = te.init(n + t), 0 === l && (h = a), console.log("ooooo", h, l), JSON.stringify({
            mi: a,
            d,
            o: h
          })
        }

        function le(e) {
          return ["qqFriends", "qzone", "fast", "friends", "timeline", "recentContact"][parseInt(e)] || "friends"
        }
        const ue = function (e, t) {
          return "boolean" == typeof e || void 0 === e[t] || e[t]
        };

        function he(e) {
          return e.route || e.__route__ || ""
        }

        function pe(e) {
          return e.route || e.__route__ || ""
        }
        const de = I(),
          ge = C();
        let fe = "";
        try {
          fe = "1.8.8-dev.7"
        } catch (e) {}
        const me = function () {
          function e() {
            const e = this;
            this.env = "production", this.cachePrefix = P, this.inited = !1, this.option = {}, this.context = {
              idenTifier: "-------"
            }, this.idenTifierChanArr = j, this.idenTifierUserArr = F, this.reportState = "WAITING", this.needCheckUrlInfo = [], this.autoProxyData = {}, this.remoteConfigInfo = {
              masterSwitch: !0,
              isOpenProxyWxApi: !1
            }, this.openTrack = function () {
              const e = this;
              this.checkFallback(), this.option.autoStart && this.startReport(), setTimeout(() => {
                e.trackLogEvents()
              }, 999)
            }, this.initRemoteConfig = function () {
              try {
                const e = this;
                ge({
                  url: "https://zhls.qq.com/open/sdk?token=".concat(this.option.token),
                  data: {},
                  header: {
                    "content-type": "json"
                  },
                  success(t) {
                    try {
                      const i = t.data;
                      if (e.remoteConfigInfo = v(e.remoteConfigInfo, i), e.track("sdk_config_info", {
                          _sdk_config_info: e.remoteConfigInfo
                        }), !e.remoteConfigInfo.masterSwitch) return;
                      e.openTrack(), e.remoteConfigInfo.isOpenProxyWxApi && e.openProxyWxApi()
                    } catch (t) {
                      e.track("sdk_error_log", {
                        _sdk_error_log: {
                          message: "request proxyConfig success",
                          type: U,
                          error: t.message
                        }
                      }), e.openTrack()
                    }
                  },
                  fail(t) {
                    console.log("request proxyConfig error：", t), e.track("sdk_error_log", {
                      _sdk_error_log: {
                        message: "request proxyConfig fail, url: https://zhls.qq.com/open/sdk?token=".concat(e.option.token),
                        type: U,
                        error: t.errMsg
                      }
                    }), e.openTrack()
                  }
                })
              } catch (e) {
                console.log("request proxyConfig error：", e), this.track("sdk_error_log", {
                  _sdk_error_log: {
                    message: "request proxyConfig error, url: https://zhls.qq.com/open/sdk?token=".concat(this.option.token),
                    type: U,
                    error: e.message
                  }
                }), this.openTrack()
              }
            }, this.openProxyWxApi = function () {
              const e = this;
              try {
                const t = l({}, this.remoteConfigInfo);
                if (delete t.masterSwitch, delete t.isOpenProxyWxApi, !Object.keys(t).length) return;
                Object.keys(t).forEach(i => {
                  e.autoProxyData[i] = {}, t[i].forEach(t => {
                    e.autoProxyData[i][t.name] = {
                      _sr_track_url: "",
                      _sr_track_body: ""
                    }, t.value.forEach(n => {
                      e.needCheckUrlInfo.push({
                        name: t.name,
                        url: n.url,
                        eventName: i,
                        grabLocation: n.grabLocation
                      })
                    })
                  })
                })
              } catch (e) {
                this.track("sdk_error_log", {
                  _sdk_error_log: {
                    message: "openProxyWxApi error",
                    type: U,
                    error: e.message
                  }
                }), console.warn("SDK下发配置接口报错：", e)
              }
            }, this.hackAutoTrack = function () {
              const e = this;
              V({
                  success(t, i) {
                    e.remoteConfigInfo.isOpenProxyWxApi && e.checkRequestUrl(i.url).forEach(n => {
                      let o;
                      if ("request" === n.grabLocation) {
                        const e = function (e) {
                          let t = "";
                          void 0 === e ? t = decodeURI(location.search) : e.split("?").length > 1 && (t = "?".concat(e.split("?")[1]));
                          const i = new Object;
                          if (-1 != t.indexOf("?"))
                            for (let e = t.substr(1).split("&"), n = 0; n < e.length; n++) i[e[n].split("=")[0]] = decodeURI(e[n].split("=")[1]);
                          return i
                        }(i.url);
                        o = v(e, i.data)
                      } else o = t.data;
                      e.autoProxyData[n.eventName][n.name]._sr_track_body = o, e.autoProxyData[n.eventName][n.name]._sr_track_url = n.url, e.ckObjectFullFill(n.eventName) && ("custom_order" == n.eventName ? e.track(n.eventName, {
                        is_sdk_auto_track: !0,
                        _auto_proxy_data: e.formatAutoData(n.eventName),
                        order: {
                          order_time: Number((new Date).getTime()),
                          order_status: "give_order"
                        }
                      }) : (e.track(n.eventName, {
                        is_sdk_auto_track: !0,
                        _auto_proxy_data: e.formatAutoData(n.eventName)
                      }), e.clearProxyData(n.eventName)))
                    })
                  }
                }, this.track.bind(this)),
                function (e, t) {
                  r || (r = t), !Z && function () {
                    try {
                      Object.defineProperty(K, "requestPayment", {
                        get() {
                          return function (e) {
                            return Y(e, "requestPayment")
                          }
                        }
                      }), Object.defineProperty(K, "requestOrderPayment", {
                        get() {
                          return function (e) {
                            return Y(e, "requestOrderPayment")
                          }
                        }
                      })
                    } catch (e) {
                      console.warn("cannot override `requestPayment`, error is: ", e)
                    } finally {
                      Z = !0
                    }
                  }(), Q.push(e)
                }({
                  onStart() {
                    e.remoteConfigInfo.isOpenProxyWxApi && (e.ckObjectFullFill("custom_order") ? e.track("custom_order", {
                      is_sdk_auto_track: !0,
                      _auto_proxy_data: e.formatAutoData("custom_order"),
                      order: {
                        order_time: Number((new Date).getTime()),
                        order_status: "pay"
                      }
                    }) : e.track("sdk_error_log", {
                      _sdk_error_log: {
                        message: "custom_order error",
                        type: "ORDER_MISSING_ERROR",
                        error: "Incomplete order"
                      }
                    }))
                  },
                  success() {
                    e.remoteConfigInfo.isOpenProxyWxApi && e.ckObjectFullFill("custom_order") && (e.track("custom_order", {
                      is_sdk_auto_track: !0,
                      _auto_proxy_data: e.formatAutoData("custom_order"),
                      order: {
                        order_time: Number((new Date).getTime()),
                        order_status: "payed"
                      }
                    }), e.clearProxyData("custom_order"))
                  },
                  fail() {
                    e.remoteConfigInfo.isOpenProxyWxApi && e.ckObjectFullFill("custom_order") && e.track("custom_order", {
                      is_sdk_auto_track: !0,
                      _auto_proxy_data: e.formatAutoData("custom_order"),
                      order: {
                        order_time: Number((new Date).getTime()),
                        order_status: "cancel_pay"
                      }
                    })
                  }
                }, this.track.bind(this))
            }, this.clearProxyData = function (e) {
              const t = this,
                i = Object.keys(this.autoProxyData[e]);
              0 !== i.length && i.forEach(i => {
                try {
                  t.autoProxyData[e][i]._sr_track_url = "", t.autoProxyData[e][i]._sr_track_body = ""
                } catch (e) {
                  t.track("sdk_error_log", {
                    _sdk_error_log: {
                      message: "clearProxyData error",
                      type: U,
                      error: e.message
                    }
                  }), console.log("clearProxyData error", e)
                }
              })
            }, this.ckObjectFullFill = function (e) {
              const t = this;
              if (void 0 === this.autoProxyData[e]) return !1;
              const i = Object.keys(this.autoProxyData[e]);
              if (0 === i.length) return !1;
              let n = !0;
              return i.forEach(i => {
                try {
                  "" == t.autoProxyData[e][i]._sr_track_body && (n = !1)
                } catch (e) {
                  t.track("sdk_error_log", {
                    _sdk_error_log: {
                      message: "ckObjectFullFill error",
                      type: U,
                      error: e.message
                    }
                  }), console.log("error ckObjectFullFill", e)
                }
              }), n
            }, this.checkRequestUrl = function (e) {
              const t = [];
              return this.needCheckUrlInfo.forEach(i => {
                e.includes(i.url) && t.push(l({}, i))
              }), t
            }, this.formatAutoData = function (e) {
              const t = this,
                i = l({}, this.autoProxyData[e]);
              return Object.keys(i).forEach(e => {
                try {
                  i[e] = d.encode(JSON.stringify(i[e]))
                } catch (e) {
                  t.track("sdk_error_log", {
                    _sdk_error_log: {
                      message: "formatAutoData error",
                      type: U,
                      error: e.message
                    }
                  }), console.log("error formatAutoData", e)
                }
              }), i
            }, this.triggerFlush = m(() => {
              e.checkAndUpload()
            }, 1e3), this.eventDataFmatter = function (t) {
              const i = +new Date,
                n = e.getPageInfo();
              if (void 0 !== e._onQueue) {
                const i = e._onQueue(t);
                g(t) ? t = i : console.warn("eventDataFmatter should return Object type")
              }
              return u(l(l({}, n), t), {
                time: i
              })
            }, this.checkRequiredOptionItem = function () {
              return !!e.option.token || (e.option.skipTokenCheck ? (console.warn("token 未配置，已跳过该检查"), !0) : (console.error("sdk.init - Option 必要参数配置缺失，请检查"), !1))
            }, this.checkVersionInfo = function () {
              if (e.setContext({
                  sr_sdk_version: e.version
                }, 1), e.isDev()) {
                const t = "https://mp.zhls.qq.com/sdk/sr-sdk-version-info.json?timesamp=".concat(Date.now());
                return e.request({}, {
                  url: t,
                  method: "GET"
                }).then(t => {
                  const i = (t.data || {})[e.name];
                  let n = !0;
                  if (i) return e.version && (1 === w(i.version.min, e.version) ? (console.error("当前SDK版本过低, 请升级！"), n = !1) : 1 === w(i.version.max, e.version) && console.warn("当前SDK有更新, 推荐升级！")), {
                    success: n,
                    data: i,
                    msg: ""
                  }
                }).catch(e => (void 0 === e && (e = {}), {
                  success: !1,
                  data: void 0,
                  msg: e.errMsg
                }))
              }
            }, this.queueInitialize = function () {
              const t = e.getServerUrl();
              return e.queue = new O({
                request(i) {
                  const n = i.events.map(t => u(l({}, t), {
                    from: "undefined" != typeof jd ? "sr-sdk-jd" : "undefined" != typeof tt ? "sr-sdk-bytedancemp" : "undefined" != typeof qq ? "sr-sdk-qqmp" : "undefined" != typeof swan ? "sr-sdk-baidu" : "undefined" != typeof dd ? "sr-sdk-dd" : "undefined" != typeof my ? "sr-sdk-alimp" : "sr-sdk-wxapp",
                    tracking_id: e.tracking_id,
                    log_id: ++e.log_id
                  }));
                  return e.setCache(R, {
                    last_tracking_id: e.tracking_id,
                    last_max_log_id: e.log_id
                  }), e.request(n, {
                    url: t,
                    method: "POST"
                  }).catch(e => (console.error("APICaller error", e), "request:fail url not in domain list" === e.msg ? u(l({}, e), {
                    success: !0
                  }) : e))
                }
              }), !0
            }, this.trackLogEvents = function () {
              const t = e.getCache(R) || {};
              return t.last_max_log_id ? (e.track("logid_events", t), !0) : (++e.log_id, !1)
            }, this.tracking_id = y(), this.log_id = -1, this.checkStaticMethods()
          }
          return e.prototype.init = function (e) {
            if (this.inited) return this;
            const t = de.getStorageSync("__SR_SDK_TRACKER___production"),
              i = t && t.USER_INFO && t.USER_INFO.app_id || "";
            let n;
            i && i !== this.option.appid && de.removeStorageSync("__SR_SDK_TRACKER___production"), this.version = fe || "", this.option = v(this.defaultOptions, this.option, e);
            const o = typeof e.autoProxy;
            if ("object" === o) {
              const t = e.autoProxy,
                i = t.openAutoTrackOpenId,
                n = void 0 === i || i,
                o = t.openSdkShareDepth,
                r = void 0 === o || o,
                s = t.openAutoTrackUnionId,
                a = void 0 === s || s,
                c = t.autoTrack,
                l = void 0 === c || c;
              this.option.proxyComponent = !0, this.option.proxyPage = !0, this.option.openAutoTrackOpenId = n, this.option.openSdkShareDepth = r, this.option.autoTrack = l, this.option.openAutoTrackUnionId = a
            }
            if ("boolean" === o && e.autoProxy && (this.option.proxyComponent = !0, this.option.proxyPage = !0, this.option.openAutoTrackOpenId = !0, this.option.openAutoTrackUnionId = !0, this.option.autoTrack = !0, this.option.openSdkShareDepth = !0), !this.checkRequiredOptionItem()) return this;
            this.cacheManagerInitialize();
            try {
              this.proxyInitialize()
            } catch (e) {
              this.errorHandle(e)
            }
            return this.queueInitialize(), this.contextInitialize(), this.inited = !0, this.checkVersionInfo(), this.initRemoteConfig(), this.option.openProxyRequest && this.hackAutoTrack(), this.option.openErrorMonitoring && (n = this.track.bind(this), z.onError(e => {
              e && n("sdk_error_log", {
                _sdk_error_log: {
                  message: "JS_RUN_ERROR",
                  type: "JS_RUN_ERROR",
                  error: e
                }
              })
            }), V({
              complete(e, t) {
                const i = e.errMsg,
                  o = e.statusCode,
                  r = e.data;
                let s = "";
                i.indexOf("timeout") > -1 ? s = "timeout" : i.indexOf("fail") > -1 ? s = "failed" : o ? o < 0 ? s = "failed" : o >= 400 && (s = "error") : s = "failed", s && n("sdk_error_log", {
                  _sdk_error_log: {
                    message: "AJAX_ERROR",
                    type: "AJAX_ERROR",
                    error: {
                      AJAX_ERROR: "request ".concat(s),
                      resStatus: o || 0,
                      resDuration: Date.now() - t.requestStartTime,
                      resData: T(r),
                      reqUrl: t.url,
                      reqMethod: t.method || "get",
                      reqParam: T(t.data),
                      errMsg: i.slice(0, 1e3)
                    }
                  }
                })
              }
            }, n)), this
          }, e.prototype.track = function (e, t) {
            if (this.remoteConfigInfo.masterSwitch) {
              const i = this.option.debug;
              JSON.stringify(t || {}).length > 5e3 && console.warn("监测到超过5000的上报日志：".concat(e));
              const n = this.eventDataFmatter(t);
              return i && console && "function" == typeof console.log && console.log("【Track】 ".concat(e), n), this.queue.add({
                type: e,
                props: n
              }), this.queue.checkQueue(), (this.queue.getItems().length || 0) > 9 && this.reportState === D ? this.flush() : this.triggerFlush(), this
            }
          }, e.prototype.setContext = function (e, t, i) {
            return void 0 === t && (t = 0), void 0 === i && (i = !1), console.warn("setContext 不在推荐使用，请用更轻便的 setUser、setChan等方法代替"), i && this.flush(), void 0 !== e.sr_sdk_version && 0 === t && delete e.sr_sdk_version, this.context = u(l(l({}, this.context), e), {
              wx_user: l(l({}, this.context.wx_user), e.wx_user || {}),
              chan: l(l({}, this.context.chan), e.chan || {})
            }), this.setIdenTifier({
              value: l({}, e),
              type: "context",
              isSr: t
            }), this
          }, e.prototype.setUser = function (e, t, i) {
            return void 0 === e && (e = {}), void 0 === t && (t = 0), void 0 === i && (i = !1), i && this.flush(), this.context = u(l({}, this.context), {
              wx_user: l(l({}, this.context.wx_user), e)
            }), this.setIdenTifier({
              value: l({}, e),
              type: "user",
              isSr: t
            }), this.setCache(E, this.context.wx_user), this
          }, e.prototype.setChan = function (e, t, i) {
            void 0 === t && (t = 0), void 0 === i && (i = !1), i && this.flush();
            const n = e.chan_id,
              o = (this.context.chan || {}).chan_id;
            return this.context = u(l({}, this.context), {
              chan: u(l(l({}, this.context.chan), e), {
                chan_id: n || o || ""
              })
            }), this.setIdenTifier({
              value: l({}, e),
              type: "chan",
              isSr: t
            }), this
          }, e.prototype.setComponent = function (e) {
            const t = e.component_id,
              i = e.component_name;
            return this.context = u(l({}, this.context), {
              component: u(l({}, e), {
                component_id: t,
                component_name: i
              })
            }), this
          }, e.prototype.clearComponent = function () {
            return delete this.context.component, this
          }, e.prototype.setActivityInfo = function (e) {
            const t = e.activity_id,
              i = e.activity_name,
              n = e.activity_type,
              o = e.activity_index;
            return this.context = u(l({}, this.context), {
              activity_info: u(l({}, e), {
                activity_id: t,
                activity_name: i,
                activity_type: n,
                activity_index: o
              })
            }), this
          }, e.prototype.clearActivityInfo = function () {
            return delete this.context.activity_info, this
          }, e.prototype.startReport = function () {
            return this.reportState = D, this.triggerFlush(), this
          }, e.prototype.resumeReport = function () {
            const e = this.getCache(A) || [];
            return this.queue.unshift(e), this.reportState === q && (this.reportState = D), this.triggerFlush(), this
          }, e.prototype.pauseReport = function () {
            return this.reportState = q, this.setCache(A, this.queue.clean()), this
          }, e.prototype.flush = function () {
            return this.queue.flush(this.context, this.getCache(N)), this
          }, e.prototype.onQueue = function (e) {
            return this._onQueue = e, this
          }, e.prototype.getInfo = function () {
            const e = {
              option: this.option,
              tracking_id: this.tracking_id,
              context: this.context,
              is_dev: this.isDev()
            };
            return "SR_SDK_INFO=".concat(d.encode(JSON.stringify(e)))
          }, e.prototype.getLocalId = function () {
            return this.context.wx_user.local_id || ""
          }, e.prototype.getWxUserInfo = function () {
            return l({}, this.context.wx_user)
          }, e.prototype.getChanInfo = function () {
            return l({}, this.context.chan)
          }, e.prototype.getPagePathInfo = function () {
            return oe() || ""
          }, e.prototype.checkStaticMethods = function () {
            if ("development" === this.env) try {
              const e = this.constructor;
              ["create"].forEach(t => {
                !e[t] && console.error("static ".concat(t, " should be implement"))
              })
            } catch (e) {
              console.error("checkStaticMethods error", e)
            }
          }, e.prototype.checkFallback = function () {
            const e = this;
            setTimeout(() => {
              e.checkAndUpload(), e.checkFallback()
            }, 1e4)
          }, e.prototype.checkAndUpload = function () {
            this.reportState === D && this.flush()
          }, e.prototype.contextInitialize = function () {
            const e = this.getUser(),
              t = this.getSystemInfo(),
              i = t.brand,
              n = t.model,
              o = t.version,
              r = t.environment,
              s = t.screenWidth,
              a = t.screenHeight,
              c = t.system,
              h = t.platform,
              p = t.SDKVersion,
              d = t.benchmarkLevel,
              g = t.locationReducedAccuracy,
              f = this.getFrameworkInfo();
            this.context = v(this.context, {
              wx_user: u(l({}, e), {
                app_id: this.option.appid
              }),
              system_info: {
                brand: i,
                model: n,
                version: o,
                environment: r,
                screenWidth: s,
                screenHeight: a,
                system: c,
                platform: h,
                SDKVersion: p,
                benchmarkLevel: d,
                LRA: g
              },
              framework_info: f,
              chan: {}
            }), this.setIdenTifier({
              value: {
                app_id: this.option.appid
              },
              type: "user",
              isSr: 1
            })
          }, e.prototype.rleitrValue = function (e, t, i) {
            const n = e.split("");
            return n[t] = i, n.join("")
          }, e.prototype.setuserchanItr = function (e, t, i) {
            const n = this,
              o = this.getCache(N) || "-----";
            Object.keys(e).forEach((e, r) => {
              "user" === t && -1 !== n.idenTifierUserArr.indexOf(e) && n.setCache(N, n.rleitrValue(o, n.idenTifierUserArr.indexOf(e), i)), "chan" === t && -1 !== n.idenTifierChanArr.indexOf(e) && (n.context.idenTifier = n.rleitrValue(n.context.idenTifier, n.idenTifierChanArr.indexOf(e), i))
            })
          }, e.prototype.setcontextItr = function (e, t) {
            e.wx_user && this.setuserchanItr(l({}, e.wx_user), "user", t), e.chan && this.setuserchanItr(l({}, e.chan), "chan", t), delete e.wx_user, delete e.chan, this.setuserchanItr(l({}, e), "chan", t)
          }, e.prototype.setIdenTifier = function (e) {
            const t = e.value,
              i = e.type,
              n = e.isSr;
            "context" === i ? this.setcontextItr(t, n) : this.setuserchanItr(t, i, n)
          }, e.prototype.getUser = function () {
            let e = this.context.wx_user || this.getCache(E) || {};
            return e.local_id && 50 === e.local_id.length || (e = {
              local_id: y()
            }, this.setIdenTifier({
              value: l({}, e),
              type: "user",
              isSr: 1
            }), this.setCache(E, e)), e
          }, e.prototype.cacheManagerInitialize = function () {
            const e = this.getCacheManager();
            this.cacheManager = e
          }, e.prototype.getCache = function (e) {
            return this.cacheManager ? (this.cacheManager.get(P) || {})[e] : (console.error(M), {})
          }, e.prototype.setCache = function (e, t) {
            let i;
            this.cacheManager || console.error(M);
            const n = l(l({}, this.cacheManager.get(P) || {}), ((i = {})[e] = t, i));
            this.cacheManager.set(P, n)
          }, e.prototype.getServerUrl = function () {
            let e = "";
            return e = "function" == typeof this.option.serverUrl ? this.option.serverUrl.call(this) : this.option.serverUrl || "https://zhls.qq.com/api/report", e + "?token=".concat(this.option.token)
          }, e.prototype.getTrackingId = function () {
            return this.tracking_id
          }, i([X], e.prototype, "init", null), i([X, ee], e.prototype, "track", null), i([X, ee], e.prototype, "setContext", null), i([X, ee], e.prototype, "setUser", null), i([X, ee], e.prototype, "setChan", null), i([X, ee], e.prototype, "setComponent", null), i([X, ee], e.prototype, "clearComponent", null), i([X, ee], e.prototype, "setActivityInfo", null), i([X, ee], e.prototype, "clearActivityInfo", null), i([X, ee], e.prototype, "startReport", null), i([X, ee], e.prototype, "resumeReport", null), i([X, ee], e.prototype, "pauseReport", null), i([X, ee], e.prototype, "flush", null), i([X, ee], e.prototype, "onQueue", null), i([X, ee], e.prototype, "getInfo", null), i([X, ee], e.prototype, "getLocalId", null), i([X, ee], e.prototype, "getWxUserInfo", null), i([X, ee], e.prototype, "getChanInfo", null), i([X, ee], e.prototype, "getPagePathInfo", null), e
        }();

        function ye(e, t, i, o) {
          void 0 === o && (o = !1);
          const r = e[t];
          e[t] = function () {
            for (var e = arguments, t = this, s = [], a = 0; a < arguments.length; a++) s[a] = e[a];
            let c = function () {
              return r && r.apply(t, s)
            };
            return o && (c = function () {
              return Promise.resolve().then(() => r.apply(t, s))
            }), i.apply(this, n([c], s))
          }
        }
        const ve = function () {},
          _e = {};
        let be = {};
        const ke = function () {
            return (new Date).getTime()
          },
          Se = function () {},
          xe = {};
        let we = {};
        const Te = function () {
            return (new Date).getTime()
          },
          Ie = ["utf8", "utf-8", "unicode-1-1-utf-8"];
        for (let e = new Uint8Array(256), t = 0; t < e.length; ++t) e[t] = t;
        const Ce = new function (e) {
          if (Ie.indexOf(e) < 0) throw new RangeError("Invalid encoding type. Only utf-8 is supported");
          this.encoding = "utf-8", this.encode = function (e) {
            if ("string" != typeof e) throw new TypeError("passed argument must be of tye string");
            for (var t = unescape(encodeURIComponent(e)), i = new Uint8Array(t.length), n = t.split(""), o = 0; o < n.length; o++) i[o] = n[o].charCodeAt(0);
            return i
          }
        }("utf-8");

        function Oe() {}
        Oe.prototype.encrypt = function (e, t) {
          return function (e, t) {
            for (var i, n = e.length, o = new Uint8Array(n), r = 0, s = 0, a = 0; a < n; ++a) s = s + t[r = r + 1 & 255] & 255, i = t[r], t[r] = t[s], t[s] = i, o[a] = e[a] ^ t[t[r] + t[s] & 255];
            return o
          }(Ce.encode(e), function (e) {
            for (var t = new Uint8Array(256), i = 0; i < 256; ++i) t[i] = i;
            let n, o = 0;
            for (i = 0; i < 256; ++i) o = o + t[i] + e[i % e.length] & 255, n = t[i], t[i] = t[o], t[o] = n;
            return t
          }(Ce.encode(t)))
        };
        const Pe = new Oe,
          Ae = {},
          Ee = function (e) {
            return e
          },
          Re = I(),
          Ne = C();
        var De = function (e) {
          function i() {
            const t = e.call(this) || this;
            return t.name = "mp", t.component = Ee, t.page = Ee, t.proxySetNavigation = function () {
              try {
                const e = Re.setNavigationBarTitle;
                Object.defineProperty(Re, "setNavigationBarTitle", {
                  get() {
                    return function (t) {
                      void 0 === t && (t = {});
                      try {
                        const e = ne();
                        try {
                          __wxConfig.page = __wxConfig.page || {}
                        } catch (e) {
                          console.error(e)
                        }
                        const i = __wxConfig.page["".concat(e.route, ".html")];
                        i && ((i.window || {}).navigationBarTitleText = t.title)
                      } catch (e) {}
                      e.call(this, t)
                    }
                  }
                })
              } catch (e) {
                console.warn("proxySetNavigation failed", e)
              }
            }, t.request = function (e, i) {
              try {
                let n = function (e) {
                  return void 0 === e && (e = {}), 0 === e.code
                };
                if ("function" == typeof t.option.onUploaded && (n = t.option.onUploaded), t.option.encrypt) {
                  const t = y(),
                    i = Pe.encrypt(JSON.stringify(e), t);
                  h.uint8ArrayToBase64(i)
                }
                return new Promise((t, o) => {
                  Ne({
                    url: i.url,
                    method: i.method || "POST",
                    data: e,
                    success(e) {
                      void 0 === e && (e = {});
                      const i = e.data,
                        o = void 0 === i ? {} : i,
                        r = n(o);
                      t({
                        success: void 0 === r || r,
                        data: o.data || o,
                        msg: o.errMsg
                      })
                    },
                    fail(e) {
                      o({
                        success: !1,
                        data: void 0,
                        msg: e.errMsg
                      })
                    }
                  })
                })
              } catch (e) {
                console.log("sdk request error", e)
              }
            }, t.defaultOptions = {
              autoProxy: !1,
              autoStart: !0,
              debug: !1,
              encrypt: !1,
              usePlugin: !1,
              proxyPage: !1,
              proxyComponent: !1,
              autoTrack: !1,
              trackApp: !0,
              openSdkShareDepth: !1,
              installFrom: "",
              openAutoTrackOpenId: !1,
              openAutoTrackUnionId: !1,
              openErrorMonitoring: !1,
              openProxyRequest: !1
            }, t.proxySetNavigation(), t
          }
          return t(i, e), i.prototype.getCacheManager = function () {
            const e = "".concat(this.env),
              t = function (t) {
                return "".concat(t, "_").concat(e)
              };
            return {
              get(e) {
                let i;
                try {
                  i = "undefined" != typeof my ? Re.getStorageSync({
                    key: t(e)
                  }).data : Re.getStorageSync(t(e))
                } catch (e) {
                  return console.error("CacheManager.get error", e), i
                }
                return i
              },
              set(e, i) {
                try {
                  "undefined" != typeof my ? Re.setStorageSync({
                    key: t(e),
                    data: i
                  }) : Re.setStorageSync(t(e), i)
                } catch (e) {
                  return console.error("CacheManager.set error", e), !1
                }
                return !0
              }
            }
          }, i.prototype.proxyInitialize = function () {
            return De.options = this.option, this.trackApp(), !0
          }, i.prototype.trackApp = function () {
            const e = this;
            let t = !1;
            Re.onAppShow(i => {
              void 0 === i && (i = {});
              const n = i,
                o = n.query,
                r = void 0 === o ? {} : o;
              let s = n.path;
              const a = n.shareTicket,
                c = e.option.openSdkShareDepth,
                h = e.option.openAutoTrackOpenId,
                p = e.option.openAutoTrackUnionId,
                d = e.option.appid,
                g = function (e) {
                  void 0 === e && (e = {});
                  const t = {};
                  if ("undefined" != typeof tt && Object.keys(e).includes("[object Object]") && delete e["[object Object]"], e.scene) {
                    try {
                      let i = decodeURIComponent(e.scene);
                      (i = i.replace("?", "").trim()).split("&").map(e => {
                        if (e) {
                          const i = e.split("="),
                            n = i[0],
                            o = i[1];
                          _(n) && (t[n] = void 0 === o || o)
                        }
                      })
                    } catch (e) {
                      console.error(e)
                    }
                    e = l(l({}, e), t)
                  }
                  return e
                }(r || {}),
                f = g.txsrShareInfoSdk || "{}",
                m = e;
              if (g && "{}" !== JSON.stringify(g)) {
                let e = "?";
                Object.entries(g).forEach((t, i) => {
                  const n = t[0],
                    o = t[1];
                  e += "".concat((0 === i ? "" : "&") + n, "=").concat(o)
                }), s += e
              }
              if (e.setChan(u(l({}, g), {
                  chan_wxapp_scene: i.scene,
                  chan_refer_app_id: (i.referrerInfo || {}).appId
                }), 1), g.chan_id && e.setChan({
                  chan_id: g.chan_id
                }, 1), c && "{}" !== f) try {
                e.setUser({
                  txsr_from_share_info: JSON.parse(decodeURIComponent(f))
                }, 1)
              } catch (e) {}
              t || (t = !0, e.option.trackApp && ue(e.option.autoProxy, "app_launch") && e.track("app_launch", {
                is_sdk_auto_track: !0,
                page: s
              }));
              const y = (e.cacheManager.get(P) || {}).USER_INFO || {},
                v = y.open_id,
                b = void 0 === v ? "" : v,
                k = y.union_id;
              if (h && !b || p && (void 0 === k || !k)) try {
                Re.login({
                  success(e) {
                    const t = e.code;
                    Ne({
                      url: "https://zhls.qq.com/wxlogin/getOpenId?appid=".concat(d, "&js_code=").concat(t),
                      data: {},
                      header: {
                        "content-type": "application/json"
                      },
                      success(e) {
                        const t = e.data,
                          i = t.openId,
                          n = t.unionId,
                          o = void 0 === n ? "" : n;
                        m.setUser({
                          open_id: i,
                          union_id: o
                        }, 1), c && a && i && m.getOpenGId(a, i)
                      }
                    })
                  }
                })
              } catch (t) {
                e.errorHandle(t)
              }
              c && a && b && e.getOpenGId(a, b), e.option.trackApp && ue(e.option.autoProxy, "app_show") && e.track("app_show", {
                is_sdk_auto_track: !0,
                page: s
              })
            }), Re.onAppHide(() => {
              e.option.trackApp && ue(e.option.autoProxy, "app_exit") && e.track("exit_wxapp", {
                is_sdk_auto_track: !0
              })
            })
          }, i.prototype.getOpenGId = function (e, t) {
            const i = this.option.appid,
              n = this;
            Re.getShareInfo({
              shareTicket: e,
              success(e) {
                const o = e.iv,
                  r = e.encryptedData;
                Ne({
                  url: "https://zhls.qq.com/wxlogin/convertData",
                  data: {
                    appid: i,
                    openid: t,
                    data: r,
                    iv: o
                  },
                  header: {
                    "content-type": "application/json"
                  },
                  success(e) {
                    const t = (e && e.data).openGId;
                    t && n.setChan({
                      openGId: t
                    }, 1)
                  }
                })
              },
              fail(e) {}
            })
          }, i.prototype.errorHandle = function (e) {
            try {
              const t = this.getServerUrl();
              this.request({
                type: "sdk api exec error",
                props: {
                  sr_sdk_version: this.version,
                  system_info: this.getSystemInfo(),
                  framework_info: this.getFrameworkInfo(),
                  message: e,
                  stack: e
                }
              }, {
                url: t,
                method: "POST"
              })
            } catch (e) {
              console.log("errorHandle error", e)
            }
          }, i.prototype.getSystemInfo = function () {
            try {
              return Re.getSystemInfoSync()
            } catch (e) {
              return {}
            }
          }, i.prototype.getFrameworkInfo = function () {
            let e, t;
            try {
              if (process && {
                  NODE_ENV: "production",
                  BASE_URL: "/"
                } && {
                  NODE_ENV: "production",
                  BASE_URL: "/"
                }.TARO_ENV && (e = "taro"), this.option.installFrom) {
                const i = String(this.option.installFrom).toLowerCase(),
                  n = /^((taro)|(uni[\-]?app)|(chameleon)|(wepy)|(mpvue))(@v?([\S]*))?/g.exec(i);
                n && n[1] && ("taro" === e && n[2] ? t = n[8] : "taro" !== e && (t = n[8], e = n[3] ? "uni-app" : n[4] || n[5] || n[6] || "unknown"))
              }
            } catch (t) {
              e = "unknown"
            }
            return {
              framework: e,
              version: t
            }
          }, i.prototype.getPageInfo = function () {
            const e = oe(),
              t = ne() || {};
            let i = se;
            const n = (t.data || {}).title || t.title;
            try {
              void 0 === n && e && !Ae[e] && (Ae[e] = !0, console.warn("页面[".concat(e, "]没有实现 title 属性，会导致部分机型下收集不到页面标题!"))), "string" == typeof n && (i = function () {
                return n
              }), "function" == typeof n && (i = n)
            } catch (e) {
              console.error("curPage.data.title 执行错误", e)
            }
            return {
              page: e,
              page_title: i()
            }
          }, i.prototype.isDev = function () {
            return "devtools" === function () {
              try {
                return "undefined" == typeof __wxConfig ? "" : __wxConfig.platform
              } catch (e) {
                console.error("getEnv failed: ", e)
              }
              return ""
            }()
          }, i.create = function () {
            let e;
            try {
              e = new i
            } catch (t) {
              e = i.prototype, console.error("new sr_sdk failed", t)
            }
            return e
          }, i
        }(me).create();
        const qe = Page,
          Me = Component;
        return Page = function (e) {
          if (De.option.proxyPage) {
            const t = function (e, t, i, n, o, r) {
              return function (s) {
                return function (e, t, i, n, o, r, s) {
                  if (ye(e, "onLoad", function (e, t) {
                      e(), this.lauchTime = ke()
                    }), ue(s, "browse_page") && ye(e, "onShow", function (e) {
                      const n = this,
                        o = function () {
                          const e = he(n);
                          n.showTime = ke();
                          const o = re.call(n, "room_id") || re.call(n, "roomId") || re.call(n, "roomid");
                          o && i({
                            room_id: o
                          }, 1), t("browse_wxapp_page", {
                            is_sdk_auto_track: !0,
                            refer_page: pe(be),
                            is_newly_open: !_e[e]
                          }), _e[e] = !0
                        };
                      e().then(o).catch(o)
                    }, !0), ue(s, "leave_page") && ye(e, "onHide", function (e) {
                      e();
                      let i = this.showTime ? ke() - this.showTime : 0;
                      i = i > 144e5 ? 0 : i, this.showTime = 0, t("leave_wxapp_page", {
                        is_sdk_auto_track: !0,
                        refer_page: pe(be),
                        stay_time: i
                      }), be = this, n({
                        refer_page: he(this)
                      })
                    }), ue(s, "leave_page") && ye(e, "onUnload", function (e) {
                      e();
                      let i = this.showTime ? ke() - this.showTime : 0;
                      i = i > 144e5 ? 0 : i, t("leave_wxapp_page", {
                        is_sdk_auto_track: !0,
                        refer_page: pe(be),
                        stay_time: i
                      }), be = this, n({
                        refer_page: he(this)
                      })
                    }), ue(s, "page_pull_down_refresh") && ye(e, "onPullDownRefresh", e => {
                      e(), t("page_pull_down_refresh", {
                        is_sdk_auto_track: !0
                      })
                    }), ue(s, "page_reach_bottom") && ye(e, "onReachBottom", e => {
                      e(), t("page_reach_bottom", {
                        is_sdk_auto_track: !0
                      })
                    }), ue(s, "page_share_app_message") && "function" == typeof e.onShareAppMessage) {
                    const i = e.onShareAppMessage || ve;
                    if (e.onShareAppMessage = function (e) {
                        void 0 === e && (e = {});
                        const n = i.call(this, e) || {};
                        try {
                          let i, o, s = n.path || oe.call(this, "share"); - 1 === s.indexOf("?") ? s += "?" : "&" !== s.slice(-1) && (s += "&"), r && (i = ce(), o = JSON.parse(i), s = "".concat(s, "txsrShareInfoSdk=").concat(encodeURIComponent(i))), t("page_share_app_message", {
                            is_sdk_auto_track: !0,
                            from_type: e.from || "未知",
                            share_to: le(e.shareTarget),
                            share_path: s,
                            share_title: n.title,
                            share_image_url: n.imageUrl,
                            refer_page: pe(be),
                            txsr_share_info_sdk: o
                          }), n.path = s
                        } catch (e) {
                          console.error("onShareAppMessage error", e)
                        }
                        return n
                      }, "function" == typeof e.onShareTimeline) {
                      const i = e.onShareTimeline || ve;
                      e.onShareTimeline = function (e) {
                        void 0 === e && (e = {});
                        const n = i.call(this, e) || {};
                        try {
                          let i = n.path || oe.call(this, "share");
                          const o = n.query || "";
                          let s, a; - 1 === i.indexOf("?") ? i += "?" : "&" !== i.slice(-1) && (i += "&"), r && (s = ce(), a = JSON.parse(s), i = "".concat(i, "txsrShareInfoSdk=").concat(encodeURIComponent(s))), t("page_share_app_message", {
                            is_sdk_auto_track: !0,
                            from_type: e.from || "未知",
                            share_to: "timeline",
                            query: o,
                            share_path: i,
                            share_title: n.title,
                            share_image_url: n.imageUrl,
                            refer_page: pe(be),
                            txsr_share_info_sdk: a
                          }), n.path = i
                        } catch (e) {
                          console.error("onShareAppMessage error", e)
                        }
                        return n
                      }
                    }
                  }
                  return o && Object.entries(e).filter(e => {
                    const t = e[0];
                    return e[1], !["onLoad", "onShow", "onReady", "onHide", "onUnload", "onPullDownRefresh", "onReachBottom", "onPageScroll", "onShareAppMessage", "onResize", "onTabItemTap"].includes(t)
                  }).forEach(i => {
                    const n = i[0];
                    "function" == typeof i[1] && ye(e, n, function (e) {
                      for (var i = arguments, o = [], r = 1; r < arguments.length; r++) o[r - 1] = i[r];
                      return ae.call(this, o, t, n), e()
                    })
                  }), e
                }(s, e, t, i, n, o, r)
              }
            }(De.track.bind(De), De.setChan.bind(De), De.setContext.bind(De), De.option.autoTrack, De.option.openSdkShareDepth, De.option.autoProxy);
            qe(t(e))
          } else qe(e)
        }, Page.after = qe.after, Component = function (e) {
          if (De.option.proxyComponent) {
            const t = function (e, t, i, n, o, r) {
              return function (s) {
                return function (e, t, i, n, o, r, s) {
                  try {
                    if (e.methods = e.methods || {}, ye(e.methods, "onLoad", function (e, t) {
                        e(), this.lauchTime = Te()
                      }), ue(s, "browse_page") && ye(e.methods, "onShow", function (e) {
                        const n = this,
                          o = function () {
                            const e = he(n);
                            n.showTime = Te();
                            const o = re.call(n, "room_id") || re.call(n, "roomId") || re.call(n, "roomid");
                            o && i({
                              room_id: o
                            }, 1), t("browse_wxapp_page", {
                              is_sdk_auto_track: !0,
                              refer_page: pe(we),
                              is_newly_open: !xe[e]
                            }), xe[e] = !0
                          };
                        e().then(o).catch(o)
                      }, !0), ue(s, "leave_page") && ye(e.methods, "onUnload", function (e) {
                        e();
                        let i = this.showTime ? Te() - this.showTime : 0;
                        i = i > 144e5 ? 0 : i, t("leave_wxapp_page", {
                          is_sdk_auto_track: !0,
                          refer_page: pe(we),
                          stay_time: i
                        }), we = this, n({
                          refer_page: he(this)
                        })
                      }), ue(s, "page_pull_down_refresh") && ye(e.methods, "onPullDownRefresh", e => {
                        e(), t("page_pull_down_refresh", {
                          is_sdk_auto_track: !0
                        })
                      }), ue(s, "page_reach_bottom") && ye(e.methods, "onReachBottom", e => {
                        e(), t("page_reach_bottom", {
                          is_sdk_auto_track: !0
                        })
                      }), ue(s, "leave_page") && ye(e.methods, "onHide", function (e) {
                        e();
                        let i = this.showTime ? Te() - this.showTime : 0;
                        i = i > 144e5 ? 0 : i, this.showTime = 0, t("leave_wxapp_page", {
                          is_sdk_auto_track: !0,
                          refer_page: pe(we),
                          stay_time: i
                        }), we = this, n({
                          refer_page: he(this)
                        })
                      }), ue(s, "page_share_app_message") && "function" == typeof e.methods.onShareAppMessage) {
                      const i = e.methods.onShareAppMessage || Se;
                      if (e.methods.onShareAppMessage = function (e) {
                          void 0 === e && (e = {});
                          const n = i.call(this, e) || {};
                          try {
                            let i, o, s = n.path || oe.call(this, "share"); - 1 === s.indexOf("?") ? s += "?" : "&" !== s.slice(-1) && (s += "&"), r && (i = ce(), o = JSON.parse(i), s = "".concat(s, "txsrShareInfoSdk=").concat(encodeURIComponent(i))), t("page_share_app_message", {
                              is_sdk_auto_track: !0,
                              from_type: e.from || "未知",
                              share_to: "friends",
                              share_path: s,
                              share_title: n.title,
                              share_image_url: n.imageUrl,
                              refer_page: pe(we),
                              txsr_share_info_sdk: o
                            }), n.path = s
                          } catch (e) {
                            console.error("onShareAppMessage error", e)
                          }
                          return n
                        }, "function" == typeof e.methods.onShareTimeline) {
                        const i = e.methods.onShareTimeline || Se;
                        e.methods.onShareTimeline = function (e) {
                          void 0 === e && (e = {});
                          const n = i.call(this, e) || {};
                          try {
                            let i = n.path || oe.call(this, "share");
                            const o = n.query || "";
                            let s, a; - 1 === i.indexOf("?") ? i += "?" : "&" !== i.slice(-1) && (i += "&"), r && (s = ce(), a = JSON.parse(s), i = "".concat(i, "txsrShareInfoSdk=").concat(encodeURIComponent(s))), t("page_share_app_message", {
                              is_sdk_auto_track: !0,
                              from_type: e.from || "未知",
                              share_to: le(e.shareTarget),
                              share_path: i,
                              query: o,
                              share_title: n.title,
                              share_image_url: n.imageUrl,
                              refer_page: pe(we),
                              txsr_share_info_sdk: a
                            }), n.path = i
                          } catch (e) {
                            console.error("onShareAppMessage error", e)
                          }
                          return n
                        }
                      }
                    }
                    e.methods && o && Object.entries(e.methods).filter(e => {
                      const t = e[0];
                      return e[1], !["onLoad", "onShow", "onReady", "onHide", "onUnload", "onPullDownRefresh", "onReachBottom", "onPageScroll", "onShareAppMessage", "onResize", "onTabItemTap", "observer"].includes(t)
                    }).forEach(i => {
                      const n = i[0];
                      "function" == typeof i[1] && ye(e.methods, n, function (e) {
                        for (var i = arguments, o = [], r = 1; r < arguments.length; r++) o[r - 1] = i[r];
                        return ae.call(this, o, t, n), e()
                      })
                    })
                  } catch (e) {
                    console.error("componentProxy error", e)
                  }
                  return e
                }(s, e, t, i, n, o, r)
              }
            }(De.track.bind(De), De.setChan.bind(De), De.setContext.bind(De), De.option.autoTrack, De.option.openSdkShareDepth, De.option.autoProxy);
            return Me(t(e))
          }
          return Me(e)
        }, Component.after = Me.after, De
      }, e.exports = t()
    },
    188: function (e) {
      e.exports = function () {
        "use strict";
        var e = function (t, i) {
          return (e = Object.setPrototypeOf || {
              __proto__: []
            }
            instanceof Array && function (e, t) {
              e.__proto__ = t
            } || function (e, t) {
              for (var i in t) t.hasOwnProperty(i) && (e[i] = t[i])
            })(t, i)
        };

        function t(t, i) {
          function n() {
            this.constructor = t
          }
          e(t, i), t.prototype = null === i ? Object.create(i) : (n.prototype = i.prototype, new n)
        }
        var i = function () {
          return (i = Object.assign || function (e) {
            for (var t, i = 1, n = arguments.length; i < n; i++)
              for (var o in t = arguments[i]) Object.prototype.hasOwnProperty.call(t, o) && (e[o] = t[o]);
            return e
          }).apply(this, arguments)
        };

        function n(e, t, i, n) {
          var o, r = arguments.length,
            s = r < 3 ? t : null === n ? n = Object.getOwnPropertyDescriptor(t, i) : n;
          if ("object" == typeof Reflect && "function" == typeof Reflect.decorate) s = Reflect.decorate(e, t, i, n);
          else
            for (var a = e.length - 1; a >= 0; a--)(o = e[a]) && (s = (r < 3 ? o(s) : r > 3 ? o(t, i, s) : o(t, i)) || s);
          return r > 3 && s && Object.defineProperty(t, i, s), s
        }

        function o() {
          for (var e = 0, t = 0, i = arguments.length; t < i; t++) e += arguments[t].length;
          var n = Array(e),
            o = 0;
          for (t = 0; t < i; t++)
            for (var r = arguments[t], s = 0, a = r.length; s < a; s++, o++) n[o] = r[s];
          return n
        }
        try {
          Object.entries || (Object.entries = function (e) {
            for (var t = Object.keys(e), i = t.length, n = new Array(i); i--;) n[i] = [t[i], e[t[i]]];
            return n
          }), Array.prototype.includes || (Array.prototype.includes = function (e) {
            return !!~this.indexOf(e)
          })
        } catch (e) {
          console.error("polyfill exec failed", e)
        }
        var r, s, a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
          c = /^(?:[A-Za-z\d+\/]{4})*?(?:[A-Za-z\d+\/]{2}(?:==)?|[A-Za-z\d+\/]{3}=?)?$/,
          l = function (e) {
            for (var t, i, n, o, r = "", s = 0, c = (e = String(e)).length % 3; s < e.length;) {
              if ((i = e.charCodeAt(s++)) > 255 || (n = e.charCodeAt(s++)) > 255 || (o = e.charCodeAt(s++)) > 255) throw new TypeError("Failed to execute 'btoa' on 'Window': The string to be encoded contains characters outside of the Latin1 range.");
              r += a.charAt((t = i << 16 | n << 8 | o) >> 18 & 63) + a.charAt(t >> 12 & 63) + a.charAt(t >> 6 & 63) + a.charAt(63 & t)
            }
            return c ? r.slice(0, c - 3) + "===".substring(c) : r
          },
          u = function (e) {
            return decodeURIComponent(function (e) {
              if (e = String(e).replace(/[\t\n\f\r ]+/g, ""), !c.test(e)) throw new TypeError("Failed to execute 'atob' on 'Window': The string to be decoded is not correctly encoded.");
              e += "==".slice(2 - (3 & e.length));
              for (var t, i, n, o = "", r = 0; r < e.length;) t = a.indexOf(e.charAt(r++)) << 18 | a.indexOf(e.charAt(r++)) << 12 | (i = a.indexOf(e.charAt(r++))) << 6 | (n = a.indexOf(e.charAt(r++))), o += 64 === i ? String.fromCharCode(t >> 16 & 255) : 64 === n ? String.fromCharCode(t >> 16 & 255, t >> 8 & 255) : String.fromCharCode(t >> 16 & 255, t >> 8 & 255, 255 & t);
              return o
            }(e).split("").map(function (e) {
              return "%" + ("00" + e.charCodeAt(0).toString(16)).slice(-2)
            }).join(""))
          },
          h = {
            uint8ArrayToBase64: function (e) {
              for (var t = [], i = 0, n = e.length; i < n; i += 4096) t.push(String.fromCharCode.apply(null, e.subarray(i, i + 4096)));
              return l(t.join(""))
            },
            encode: function (e) {
              return (t = e, l(encodeURIComponent(t).replace(/%([0-9A-F]{2})/g, function (e, t) {
                var i;
                return i = "0x" + t, String.fromCharCode(i)
              }))).replace(/=/g, "").replace(/\+/g, "-").replace(/\//g, "_");
              var t
            },
            decode: function (e) {
              var t = (e = e.replace(/\-/g, "+").replace(/_/g, "/")).length % 4;
              return t > 0 && (e += "====".substring(t)), u(e)
            }
          },
          p = Object.prototype.toString,
          d = h,
          g = function (e) {
            return "[object Object]" === p.call(e)
          },
          f = function (e) {
            return "[object Array]" === p.call(e)
          },
          m = function (e, t) {
            var i;
            void 0 === t && (t = 0);
            var n = [];
            return function () {
              for (var o = arguments, r = [], s = 0; s < arguments.length; s++) r[s] = o[s];
              return clearTimeout(i), i = setTimeout(function () {
                var t = e.apply(void 0, r);
                n.forEach(function (e) {
                  return e(t)
                }), n = []
              }, t), new Promise(function (e) {
                return n.push(e)
              })
            }
          },
          y = function () {
            return Date.now() + "-" + "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (e) {
              var t = 16 * Math.random() | 0;
              return ("x" == e ? t : 3 & t | 8).toString(16)
            })
          },
          v = function () {
            for (var e = arguments, t = [], i = 0; i < arguments.length; i++) t[i] = e[i];
            return 0 === t.length ? {} : t.length < 2 ? t[0] : t.reduce(function (e, t) {
              if (!g(e) || !g(t)) return console.error("deepMerge arguments only access object"), e;
              var i = e || {};
              return Object.entries(t).forEach(function (t) {
                var n = t[0],
                  r = t[1];
                if (void 0 !== r)
                  if (e[n])
                    if (f(e[n])) {
                      if (!f(r)) return void(i[n] = r);
                      var s = f(r) ? r : [r];
                      i[n] = o(e[n], s)
                    } else g(e[n]) ? i[n] = v(e[n], r) : i[n] = r;
                else i[n] = r
              }), i
            })
          },
          _ = function (e) {
            return !!/^[a-zA-Z\$_][a-zA-Z\d_]*$/.test(e)
          },
          b = /^v?(?:\d+)(\.(?:[x*]|\d+)(\.(?:[x*]|\d+)(\.(?:[x*]|\d+))?(?:-[\da-z\-]+(?:\.[\da-z\-]+)*)?(?:\+[\da-z\-]+(?:\.[\da-z\-]+)*)?)?)?$/i,
          k = function (e) {
            if ("string" != typeof e) throw new TypeError("Invalid argument expected string");
            if (!b.test(e)) throw new Error("Invalid argument not valid semver ('" + e + "' received)")
          },
          S = function (e) {
            return isNaN(Number(e)) ? e : Number(e)
          },
          x = function (e) {
            var t, i, n = e.replace(/^v/, "").replace(/\+.*$/, ""),
              o = (i = "-", -1 === (t = n).indexOf(i) ? t.length : t.indexOf(i)),
              r = n.substring(0, o).split(".");
            return r.push(n.substring(o + 1)), r
          },
          w = function (e, t) {
            [e, t].forEach(k);
            for (var i = x(e), n = x(t), o = 0; o < Math.max(i.length - 1, n.length - 1); o++) {
              var r = parseInt(i[o] || 0, 10),
                s = parseInt(n[o] || 0, 10);
              if (r > s) return 1;
              if (s > r) return -1
            }
            var a = i[i.length - 1],
              c = n[n.length - 1];
            if (a && c) {
              var l = a.split(".").map(S),
                u = c.split(".").map(S);
              for (o = 0; o < Math.max(l.length, u.length); o++) {
                if (void 0 === l[o] || "string" == typeof u[o] && "number" == typeof l[o]) return -1;
                if (void 0 === u[o] || "string" == typeof l[o] && "number" == typeof u[o]) return 1;
                if (l[o] > u[o]) return 1;
                if (u[o] > l[o]) return -1
              }
            } else if (a || c) return a ? -1 : 1;
            return 0
          },
          T = function (e) {
            if ("string" == typeof e) return e;
            try {
              return (JSON.stringify(e, (t = [], i = [], function (e, n) {
                if (n instanceof Error) return "Error.message: " + n.message + " \n  Error.stack: " + n.stack;
                if ("object" == typeof n && null !== n) {
                  var o = t.indexOf(n);
                  if (-1 !== o) return "[Circular " + i[o] + "]";
                  t.push(n), i.push(e || "root")
                }
                return n
              }), 4) || "undefined").replace(/"/gim, "")
            } catch (e) {
              return "error happen when sdk stringify: \n " + e.message + " \n " + e.stack
            }
            var t, i
          },
          I = function () {
            return "undefined" != typeof jd ? jd : "undefined" != typeof tt ? tt : "undefined" != typeof qq ? qq : "undefined" != typeof swan ? swan : "undefined" != typeof dd ? dd : "undefined" != typeof my ? my : wx
          },
          C = function () {
            return "undefined" != typeof dd ? dd.httpRequest : I().request
          },
          O = function (e) {
            function n(t) {
              var i = e.call(this, t.request) || this;
              return i.stack = [], i.initialize = function () {
                return Promise.resolve(!0)
              }, i.add = function (e) {
                i.stack.push(e)
              }, i.getItems = function () {
                return i.stack
              }, i.unshift = function (e) {
                var t;
                return (t = i.stack).unshift.apply(t, e)
              }, i.clean = function () {
                var e = i.stack;
                return i.stack = [], e
              }, i.checkQueue = function () {
                i.stack.length > 100 && (i.stack = i.stack.slice(-100))
              }, i.option = t, i.initialize(), i
            }
            return t(n, e), n.prototype.flush = function (e, t) {
              var n = this;
              if (void 0 === e && (e = {}), this.stack.length) {
                var r = JSON.parse(JSON.stringify(e));
                r.idenTifier = r.idenTifier + t;
                var s = this.stack.map(function (e) {
                  return e.props = i(i({}, e.props), r), e
                });
                this.stack = [], this.request({
                  events: s
                }).then(function (e) {
                  e.success || (n.stack = o(n.stack, s))
                }).catch(function () {
                  n.stack = o(n.stack, s)
                })
              }
            }, n
          }(function (e) {
            this.delay = 100, this.upload = m(e, this.delay), this.request = e
          }),
          P = "__SR_SDK_TRACKER__",
          A = "TRACKS",
          E = "USER_INFO",
          R = "LOGID_EVENTS",
          N = "IDENTIFIERUSER",
          D = "__GDT_VID__",
          q = "__QZ_GDT__",
          M = "WAITING",
          U = "REPORTING",
          j = "PAUSED",
          F = {
            MISS: "should exec cacheManagerInitialize first"
          },
          L = "SDK_INTERNAL_ERROR",
          G = "JS_RUN_ERROR",
          B = "AJAX_ERROR",
          H = "ORDER_MISSING_ERROR",
          W = ["page", "page_title", "time", "chan_wxapp_scene", "chan_id", "chan_refer_app_id", "room_id"],
          V = ["app_id", "open_id", "user_id", "union_id", "local_id"],
          z = I(),
          K = [],
          Q = z.request,
          J = function (e) {
            return K.forEach(function (t) {
              var i;
              try {
                e.requestStartTime = Date.now(), null === (i = t.onStart) || void 0 === i || i.call(t, e)
              } catch (e) {}
            }), Q(i(i({}, e), {
              success: function (t) {
                var i;
                K.forEach(function (i) {
                  var n;
                  try {
                    null === (n = i.success) || void 0 === n || n.call(i, t, e)
                  } catch (e) {
                    try {
                      r("sdk_error_log", {
                        _sdk_error_log: {
                          message: "request success error",
                          type: L,
                          error: e.message
                        }
                      })
                    } catch (e) {}
                  }
                }), null === (i = e.success) || void 0 === i || i.call(e, t)
              },
              fail: function (t) {
                var i;
                K.forEach(function (i) {
                  var n;
                  try {
                    null === (n = i.fail) || void 0 === n || n.call(i, t, e)
                  } catch (e) {
                    try {
                      r("sdk_error_log", {
                        _sdk_error_log: {
                          message: "request fail error",
                          type: L,
                          error: e.message
                        }
                      })
                    } catch (e) {}
                  }
                }), null === (i = e.fail) || void 0 === i || i.call(e, t)
              },
              complete: function (t) {
                var i;
                K.forEach(function (i) {
                  var n;
                  try {
                    null === (n = i.complete) || void 0 === n || n.call(i, t, e)
                  } catch (e) {
                    try {
                      r("sdk_error_log", {
                        _sdk_error_log: {
                          message: "request complete error",
                          type: L,
                          error: e.message
                        }
                      })
                    } catch (e) {}
                  }
                }), null === (i = e.complete) || void 0 === i || i.call(e, t)
              }
            }))
          },
          $ = !1,
          Y = function (e, t) {
            r || (r = t), !$ && function () {
              try {
                Object.defineProperty(z, "request", {
                  get: function () {
                    return J
                  }
                })
              } catch (e) {
                console.warn("cannot override `request`, error is: ", e)
              } finally {
                $ = !0
              }
            }(), K.push(e)
          },
          Z = I(),
          X = I(),
          ee = [],
          te = X.requestPayment,
          ie = X.requestOrderPayment,
          ne = function (e, t) {
            var n = te;
            return "requestOrderPayment" == t && (n = ie), ee.forEach(function (t) {
              var i;
              try {
                null === (i = t.onStart) || void 0 === i || i.call(t, e)
              } catch (e) {
                try {
                  s("sdk_error_log", {
                    _sdk_error_log: {
                      message: "requestPayment onStart error",
                      type: L,
                      error: e.message
                    }
                  })
                } catch (e) {}
              }
            }), n(i(i({}, e), {
              success: function (t) {
                var i;
                ee.forEach(function (i) {
                  var n;
                  try {
                    null === (n = i.success) || void 0 === n || n.call(i, t, e)
                  } catch (e) {
                    try {
                      s("sdk_error_log", {
                        _sdk_error_log: {
                          message: "requestPayment success error",
                          type: L,
                          error: e.message
                        }
                      })
                    } catch (e) {}
                  }
                }), null === (i = e.success) || void 0 === i || i.call(e, t)
              },
              fail: function (t) {
                var i;
                ee.forEach(function (i) {
                  var n;
                  try {
                    null === (n = i.fail) || void 0 === n || n.call(i, t, e)
                  } catch (e) {
                    try {
                      s("sdk_error_log", {
                        _sdk_error_log: {
                          message: "requestPayment fail error",
                          type: L,
                          error: e.message
                        }
                      })
                    } catch (e) {}
                  }
                }), null === (i = e.fail) || void 0 === i || i.call(e, t)
              }
            }))
          },
          oe = !1,
          re = function (e, t) {
            s || (s = t), !oe && function () {
              try {
                Object.defineProperty(X, "requestPayment", {
                  get: function () {
                    return function (e) {
                      return ne(e, "requestPayment")
                    }
                  }
                }), Object.defineProperty(X, "requestOrderPayment", {
                  get: function () {
                    return function (e) {
                      return ne(e, "requestOrderPayment")
                    }
                  }
                })
              } catch (e) {
                console.warn("cannot override `requestPayment`, error is: ", e)
              } finally {
                oe = !0
              }
            }(), ee.push(e)
          },
          se = function (e, t, i) {
            var n = i.value;
            return i.value = function () {
              var e;
              try {
                e = n.apply(this, arguments)
              } catch (e) {
                try {
                  console.error("Calling " + t + " error with", arguments), console.error(e);
                  var i = this.getServerUrl();
                  this.request({
                    type: "sdk api exec error",
                    props: {
                      sr_sdk_version: this.version,
                      system_info: this.getSystemInfo(),
                      framework_info: this.getFrameworkInfo(),
                      message: (e || {}).message || e,
                      stack: (e || {}).stack
                    }
                  }, {
                    url: i,
                    method: "POST"
                  })
                } catch (e) {}
              }
              return e
            }, i
          },
          ae = function (e, t, i) {
            var n = i.value;
            return i.value = function () {
              if (this.inited) return n.apply(this, arguments);
              console.error("请先完成初始化")
            }, i
          },
          ce = function () {
            function e() {}
            return e.AddUnsigned = function (e, t) {
              var i, n, o, r, s;
              return o = 2147483648 & e, r = 2147483648 & t, s = (1073741823 & e) + (1073741823 & t), (i = 1073741824 & e) & (n = 1073741824 & t) ? 2147483648 ^ s ^ o ^ r : i | n ? 1073741824 & s ? 3221225472 ^ s ^ o ^ r : 1073741824 ^ s ^ o ^ r : s ^ o ^ r
            }, e.FF = function (e, t, i, n, o, r, s) {
              return e = this.AddUnsigned(e, this.AddUnsigned(this.AddUnsigned(this.F(t, i, n), o), s)), this.AddUnsigned(this.RotateLeft(e, r), t)
            }, e.GG = function (e, t, i, n, o, r, s) {
              return e = this.AddUnsigned(e, this.AddUnsigned(this.AddUnsigned(this.G(t, i, n), o), s)), this.AddUnsigned(this.RotateLeft(e, r), t)
            }, e.HH = function (e, t, i, n, o, r, s) {
              return e = this.AddUnsigned(e, this.AddUnsigned(this.AddUnsigned(this.H(t, i, n), o), s)), this.AddUnsigned(this.RotateLeft(e, r), t)
            }, e.II = function (e, t, i, n, o, r, s) {
              return e = this.AddUnsigned(e, this.AddUnsigned(this.AddUnsigned(this.I(t, i, n), o), s)), this.AddUnsigned(this.RotateLeft(e, r), t)
            }, e.ConvertToWordArray = function (e) {
              for (var t, i = e.length, n = i + 8, o = 16 * ((n - n % 64) / 64 + 1), r = Array(o - 1), s = 0, a = 0; a < i;) s = a % 4 * 8, r[t = (a - a % 4) / 4] = r[t] | e.charCodeAt(a) << s, a++;
              return s = a % 4 * 8, r[t = (a - a % 4) / 4] = r[t] | 128 << s, r[o - 2] = i << 3, r[o - 1] = i >>> 29, r
            }, e.WordToHex = function (e) {
              var t, i = "",
                n = "";
              for (t = 0; t <= 3; t++) i += (n = "0" + (e >>> 8 * t & 255).toString(16)).substr(n.length - 2, 2);
              return i
            }, e.Utf8Encode = function (e) {
              var t, i = "";
              e = e.replace(/\r\n/g, "\n");
              for (var n = 0; n < e.length; n++)(t = e.charCodeAt(n)) < 128 ? i += String.fromCharCode(t) : t > 127 && t < 2048 ? (i += String.fromCharCode(t >> 6 | 192), i += String.fromCharCode(63 & t | 128)) : (i += String.fromCharCode(t >> 12 | 224), i += String.fromCharCode(t >> 6 & 63 | 128), i += String.fromCharCode(63 & t | 128));
              return i
            }, e.init = function (e) {
              for ("string" != typeof e && (e = JSON.stringify(e)), this._string = this.Utf8Encode(e), this.x = this.ConvertToWordArray(this._string), this.a = 1732584193, this.b = 4023233417, this.c = 2562383102, this.d = 271733878, this.k = 0; this.k < this.x.length; this.k += 16) this.AA = this.a, this.BB = this.b, this.CC = this.c, this.DD = this.d, this.a = this.FF(this.a, this.b, this.c, this.d, this.x[this.k], this.S11, 3614090360), this.d = this.FF(this.d, this.a, this.b, this.c, this.x[this.k + 1], this.S12, 3905402710), this.c = this.FF(this.c, this.d, this.a, this.b, this.x[this.k + 2], this.S13, 606105819), this.b = this.FF(this.b, this.c, this.d, this.a, this.x[this.k + 3], this.S14, 3250441966), this.a = this.FF(this.a, this.b, this.c, this.d, this.x[this.k + 4], this.S11, 4118548399), this.d = this.FF(this.d, this.a, this.b, this.c, this.x[this.k + 5], this.S12, 1200080426), this.c = this.FF(this.c, this.d, this.a, this.b, this.x[this.k + 6], this.S13, 2821735955), this.b = this.FF(this.b, this.c, this.d, this.a, this.x[this.k + 7], this.S14, 4249261313), this.a = this.FF(this.a, this.b, this.c, this.d, this.x[this.k + 8], this.S11, 1770035416), this.d = this.FF(this.d, this.a, this.b, this.c, this.x[this.k + 9], this.S12, 2336552879), this.c = this.FF(this.c, this.d, this.a, this.b, this.x[this.k + 10], this.S13, 4294925233), this.b = this.FF(this.b, this.c, this.d, this.a, this.x[this.k + 11], this.S14, 2304563134), this.a = this.FF(this.a, this.b, this.c, this.d, this.x[this.k + 12], this.S11, 1804603682), this.d = this.FF(this.d, this.a, this.b, this.c, this.x[this.k + 13], this.S12, 4254626195), this.c = this.FF(this.c, this.d, this.a, this.b, this.x[this.k + 14], this.S13, 2792965006), this.b = this.FF(this.b, this.c, this.d, this.a, this.x[this.k + 15], this.S14, 1236535329), this.a = this.GG(this.a, this.b, this.c, this.d, this.x[this.k + 1], this.S21, 4129170786), this.d = this.GG(this.d, this.a, this.b, this.c, this.x[this.k + 6], this.S22, 3225465664), this.c = this.GG(this.c, this.d, this.a, this.b, this.x[this.k + 11], this.S23, 643717713), this.b = this.GG(this.b, this.c, this.d, this.a, this.x[this.k], this.S24, 3921069994), this.a = this.GG(this.a, this.b, this.c, this.d, this.x[this.k + 5], this.S21, 3593408605), this.d = this.GG(this.d, this.a, this.b, this.c, this.x[this.k + 10], this.S22, 38016083), this.c = this.GG(this.c, this.d, this.a, this.b, this.x[this.k + 15], this.S23, 3634488961), this.b = this.GG(this.b, this.c, this.d, this.a, this.x[this.k + 4], this.S24, 3889429448), this.a = this.GG(this.a, this.b, this.c, this.d, this.x[this.k + 9], this.S21, 568446438), this.d = this.GG(this.d, this.a, this.b, this.c, this.x[this.k + 14], this.S22, 3275163606), this.c = this.GG(this.c, this.d, this.a, this.b, this.x[this.k + 3], this.S23, 4107603335), this.b = this.GG(this.b, this.c, this.d, this.a, this.x[this.k + 8], this.S24, 1163531501), this.a = this.GG(this.a, this.b, this.c, this.d, this.x[this.k + 13], this.S21, 2850285829), this.d = this.GG(this.d, this.a, this.b, this.c, this.x[this.k + 2], this.S22, 4243563512), this.c = this.GG(this.c, this.d, this.a, this.b, this.x[this.k + 7], this.S23, 1735328473), this.b = this.GG(this.b, this.c, this.d, this.a, this.x[this.k + 12], this.S24, 2368359562), this.a = this.HH(this.a, this.b, this.c, this.d, this.x[this.k + 5], this.S31, 4294588738), this.d = this.HH(this.d, this.a, this.b, this.c, this.x[this.k + 8], this.S32, 2272392833), this.c = this.HH(this.c, this.d, this.a, this.b, this.x[this.k + 11], this.S33, 1839030562), this.b = this.HH(this.b, this.c, this.d, this.a, this.x[this.k + 14], this.S34, 4259657740), this.a = this.HH(this.a, this.b, this.c, this.d, this.x[this.k + 1], this.S31, 2763975236), this.d = this.HH(this.d, this.a, this.b, this.c, this.x[this.k + 4], this.S32, 1272893353), this.c = this.HH(this.c, this.d, this.a, this.b, this.x[this.k + 7], this.S33, 4139469664), this.b = this.HH(this.b, this.c, this.d, this.a, this.x[this.k + 10], this.S34, 3200236656), this.a = this.HH(this.a, this.b, this.c, this.d, this.x[this.k + 13], this.S31, 681279174), this.d = this.HH(this.d, this.a, this.b, this.c, this.x[this.k], this.S32, 3936430074), this.c = this.HH(this.c, this.d, this.a, this.b, this.x[this.k + 3], this.S33, 3572445317), this.b = this.HH(this.b, this.c, this.d, this.a, this.x[this.k + 6], this.S34, 76029189), this.a = this.HH(this.a, this.b, this.c, this.d, this.x[this.k + 9], this.S31, 3654602809), this.d = this.HH(this.d, this.a, this.b, this.c, this.x[this.k + 12], this.S32, 3873151461), this.c = this.HH(this.c, this.d, this.a, this.b, this.x[this.k + 15], this.S33, 530742520), this.b = this.HH(this.b, this.c, this.d, this.a, this.x[this.k + 2], this.S34, 3299628645), this.a = this.II(this.a, this.b, this.c, this.d, this.x[this.k], this.S41, 4096336452), this.d = this.II(this.d, this.a, this.b, this.c, this.x[this.k + 7], this.S42, 1126891415), this.c = this.II(this.c, this.d, this.a, this.b, this.x[this.k + 14], this.S43, 2878612391), this.b = this.II(this.b, this.c, this.d, this.a, this.x[this.k + 5], this.S44, 4237533241), this.a = this.II(this.a, this.b, this.c, this.d, this.x[this.k + 12], this.S41, 1700485571), this.d = this.II(this.d, this.a, this.b, this.c, this.x[this.k + 3], this.S42, 2399980690), this.c = this.II(this.c, this.d, this.a, this.b, this.x[this.k + 10], this.S43, 4293915773), this.b = this.II(this.b, this.c, this.d, this.a, this.x[this.k + 1], this.S44, 2240044497), this.a = this.II(this.a, this.b, this.c, this.d, this.x[this.k + 8], this.S41, 1873313359), this.d = this.II(this.d, this.a, this.b, this.c, this.x[this.k + 15], this.S42, 4264355552), this.c = this.II(this.c, this.d, this.a, this.b, this.x[this.k + 6], this.S43, 2734768916), this.b = this.II(this.b, this.c, this.d, this.a, this.x[this.k + 13], this.S44, 1309151649), this.a = this.II(this.a, this.b, this.c, this.d, this.x[this.k + 4], this.S41, 4149444226), this.d = this.II(this.d, this.a, this.b, this.c, this.x[this.k + 11], this.S42, 3174756917), this.c = this.II(this.c, this.d, this.a, this.b, this.x[this.k + 2], this.S43, 718787259), this.b = this.II(this.b, this.c, this.d, this.a, this.x[this.k + 9], this.S44, 3951481745), this.a = this.AddUnsigned(this.a, this.AA), this.b = this.AddUnsigned(this.b, this.BB), this.c = this.AddUnsigned(this.c, this.CC), this.d = this.AddUnsigned(this.d, this.DD);
              return (this.WordToHex(this.a) + this.WordToHex(this.b) + this.WordToHex(this.c) + this.WordToHex(this.d)).toLowerCase()
            }, e.x = Array(), e.S11 = 7, e.S12 = 12, e.S13 = 17, e.S14 = 22, e.S21 = 5, e.S22 = 9, e.S23 = 14, e.S24 = 20, e.S31 = 4, e.S32 = 11, e.S33 = 16, e.S34 = 23, e.S41 = 6, e.S42 = 10, e.S43 = 15, e.S44 = 21, e.RotateLeft = function (e, t) {
              return e << t | e >>> 32 - t
            }, e.F = function (e, t, i) {
              return e & t | ~e & i
            }, e.G = function (e, t, i) {
              return e & i | t & ~i
            }, e.H = function (e, t, i) {
              return e ^ t ^ i
            }, e.I = function (e, t, i) {
              return t ^ (e | ~i)
            }, e
          }(),
          le = I();

        function ue() {
          var e = getCurrentPages() || "";
          return e[e.length - 1] || ""
        }

        function he(e) {
          var t = "/";
          try {
            var i = ue();
            if (!i) return i;
            var n, o = i.route || i.__route__,
              r = i.options || {};
            for (var s in n = i.options || {}, t = o + "?", r) "share" === e && "txsrShareInfoSdk" === s || _(s) && n[s] && (t += s + "=" + r[s] + "&");
            t = t.substring(0, t.length - 1)
          } catch (e) {
            console.error("getCurrentPageUrlWithArgs error", e)
          }
          return t
        }

        function pe(e) {
          try {
            var t = ue();
            if (!t) return t;
            return t.options, (t.options || {})[e] || ""
          } catch (e) {
            console.error("getCurrentPageKey error", e)
          }
          return "/"
        }

        function de() {
          try {
            return ("undefined" != typeof tt ? function () {
              var e, t = ue();
              try {
                var i = t.route || t.__route__,
                  n = "";
                return n = "undefined" != typeof __ttConfig ? __ttConfig.global.window.navigationBarTitleText : TMAConfig.global.window.navigationBarTitleText, (t ? null === (e = __allConfig__[i]) || void 0 === e ? void 0 : e.navigationBarTitleText : "") || n
              } catch (e) {}
            }() : "undefined" != typeof jd ? function () {
              var e, t, i = ue();
              try {
                var n = __jdConfig.global.window.navigationBarTitleText;
                return (i ? ((null === (t = null === (e = __jdConfig.page) || void 0 === e ? void 0 : e[i.route + ".html"]) || void 0 === t ? void 0 : t.window) || {}).navigationBarTitleText : "") || n
              } catch (e) {}
            }() : function () {
              var e, t, i, n = ue();
              try {
                var o = __wxConfig.global.window.navigationBarTitleText,
                  r = n ? ((null === (t = null === (e = __wxConfig.page) || void 0 === e ? void 0 : e[n.route + ".html"]) || void 0 === t ? void 0 : t.window) || {}).navigationBarTitleText : "",
                  s = null === (i = null === __wxAppCode__ || void 0 === __wxAppCode__ ? void 0 : __wxAppCode__[n.route + ".json"]) || void 0 === i ? void 0 : i.navigationBarTitleText;
                return r || s || o
              } catch (e) {}
            }()) || "未知"
          } catch (e) {}
          return "未知"
        }

        function ge() {
          return "devtools" === function () {
            try {
              return "undefined" == typeof __wxConfig ? "" : __wxConfig.platform
            } catch (e) {
              console.error("getEnv failed: ", e)
            }
            return ""
          }()
        }

        function fe(e, t, n) {
          try {
            var o = e[0],
              r = void 0 === o ? {} : o;
            if (r) switch (r.type) {
              case "tap":
              case "longpress":
              case "longtap":
              case "confirm":
                var s = (r.currentTarget || {}).dataset,
                  a = void 0 === s ? {} : s;
                0 == Object.keys(a).length && (a = r.target.dataset);
                var c = this || {},
                  l = c.is,
                  u = void 0 === l ? "" : l;
                c.data, t("element", i({
                  is_sdk_auto_track: !0,
                  is: u,
                  type: r.type,
                  element_id: "#" + n
                }, a))
            }
          } catch (e) {
            console.error("elementEventTrack error", e)
          }
        }

        function me() {
          var e, t = (ue() || {}).route || "";
          try {
            e = le.getStorageSync(P + "_production")
          } catch (e) {
            console.error("CacheManager.get error", e)
          }
          var i = e.USER_INFO || {},
            n = i.local_id,
            o = i.txsr_from_share_info,
            r = void 0 === o ? {} : o,
            s = r.mi,
            a = void 0 === s ? "" : s,
            c = r.d,
            l = void 0 === c ? 0 : c,
            u = r.o,
            h = void 0 === u ? "" : u,
            p = ce.init(n + t),
            d = "" !== a && p === a ? l : l + 1;
          return a = ce.init(n + t), 0 === l && (h = a), console.log("ooooo", h, l), JSON.stringify({
            mi: a,
            d,
            o: h
          })
        }

        function ye(e) {
          return ["qqFriends", "qzone", "fast", "friends", "timeline", "recentContact"][parseInt(e)] || "friends"
        }
        var ve = function (e, t) {
          return "boolean" == typeof e ? e : void 0 === (null == e ? void 0 : e[t]) || (null == e ? void 0 : e[t])
        };

        function _e(e) {
          return e.route || e.__route__ || ""
        }

        function be(e) {
          return e.route || e.__route__ || ""
        }
        var ke = I(),
          Se = C(),
          xe = "https://api.datanexus.qq.com/youshu/api/report",
          we = "";
        try {
          we = "2.1.1"
        } catch (e) {}
        var Te = function () {
          function e() {
            var e = this;
            this.env = "production", this.cachePrefix = P, this.inited = !1, this.option = {}, this.context = {
              idenTifier: "-------"
            }, this.idenTifierChanArr = W, this.idenTifierUserArr = V, this.reportState = M, this.needCheckUrlInfo = [], this.autoProxyData = {}, this.remoteConfigInfo = {
              masterSwitch: !0,
              isOpenProxyWxApi: !1
            }, this.openTrack = function () {
              var e = this;
              this.checkFallback(), this.option.autoStart && this.startReport(), setTimeout(function () {
                e.trackLogEvents()
              }, 999)
            }, this.initRemoteConfig = function () {
              try {
                var e = this;
                Se({
                  url: "https://zhls.qq.com/open/sdk?token=" + this.option.token,
                  data: {},
                  header: {
                    "content-type": "json"
                  },
                  success: function (t) {
                    try {
                      var i = t.data;
                      if (e.remoteConfigInfo = v(e.remoteConfigInfo, i), e.track("sdk_config_info", {
                          _sdk_config_info: e.remoteConfigInfo
                        }), !e.remoteConfigInfo.masterSwitch) return;
                      e.openTrack(), e.remoteConfigInfo.isOpenProxyWxApi && e.openProxyWxApi()
                    } catch (t) {
                      e.track("sdk_error_log", {
                        _sdk_error_log: {
                          message: "request proxyConfig success",
                          type: L,
                          error: t.message
                        }
                      }), e.openTrack()
                    }
                  },
                  fail: function (t) {
                    console.log("request proxyConfig error：", t), e.track("sdk_error_log", {
                      _sdk_error_log: {
                        message: "request proxyConfig fail, url: https://zhls.qq.com/open/sdk?token=" + e.option.token,
                        type: L,
                        error: t.errMsg
                      }
                    }), e.openTrack()
                  }
                })
              } catch (e) {
                console.log("request proxyConfig error：", e), this.track("sdk_error_log", {
                  _sdk_error_log: {
                    message: "request proxyConfig error, url: https://zhls.qq.com/open/sdk?token=" + this.option.token,
                    type: L,
                    error: e.message
                  }
                }), this.openTrack()
              }
            }, this.openProxyWxApi = function () {
              var e = this;
              try {
                var t = i({}, this.remoteConfigInfo);
                if (delete t.masterSwitch, delete t.isOpenProxyWxApi, !Object.keys(t).length) return;
                Object.keys(t).forEach(function (i) {
                  e.autoProxyData[i] = {}, t[i].forEach(function (t) {
                    e.autoProxyData[i][t.name] = {
                      _sr_track_url: "",
                      _sr_track_body: ""
                    }, t.value.forEach(function (n) {
                      e.needCheckUrlInfo.push({
                        name: t.name,
                        url: n.url,
                        eventName: i,
                        grabLocation: n.grabLocation
                      })
                    })
                  })
                })
              } catch (e) {
                this.track("sdk_error_log", {
                  _sdk_error_log: {
                    message: "openProxyWxApi error",
                    type: L,
                    error: e.message
                  }
                }), console.warn("SDK下发配置接口报错：", e)
              }
            }, this.hackAutoTrack = function () {
              var e = this;
              Y({
                success: function (t, i) {
                  e.remoteConfigInfo.isOpenProxyWxApi && e.checkRequestUrl(i.url).forEach(function (n) {
                    var o;
                    if ("request" === n.grabLocation) {
                      var r = function (e) {
                        var t = "";
                        void 0 === e ? t = decodeURI(location.search) : e.split("?").length > 1 && (t = "?" + e.split("?")[1]);
                        var i = new Object;
                        if (-1 != t.indexOf("?"))
                          for (var n = t.substr(1).split("&"), o = 0; o < n.length; o++) i[n[o].split("=")[0]] = decodeURI(n[o].split("=")[1]);
                        return i
                      }(i.url);
                      o = v(r, i.data)
                    } else o = t.data;
                    e.autoProxyData[n.eventName][n.name]._sr_track_body = o, e.autoProxyData[n.eventName][n.name]._sr_track_url = n.url, e.ckObjectFullFill(n.eventName) && ("custom_order" == n.eventName ? e.track(n.eventName, {
                      is_sdk_auto_track: !0,
                      _auto_proxy_data: e.formatAutoData(n.eventName),
                      order: {
                        order_time: Number((new Date).getTime()),
                        order_status: "give_order"
                      }
                    }) : (e.track(n.eventName, {
                      is_sdk_auto_track: !0,
                      _auto_proxy_data: e.formatAutoData(n.eventName)
                    }), e.clearProxyData(n.eventName)))
                  })
                }
              }, this.track.bind(this)), re({
                onStart: function () {
                  e.remoteConfigInfo.isOpenProxyWxApi && (e.ckObjectFullFill("custom_order") ? e.track("custom_order", {
                    is_sdk_auto_track: !0,
                    _auto_proxy_data: e.formatAutoData("custom_order"),
                    order: {
                      order_time: Number((new Date).getTime()),
                      order_status: "pay"
                    }
                  }) : e.track("sdk_error_log", {
                    _sdk_error_log: {
                      message: "custom_order error",
                      type: H,
                      error: "Incomplete order"
                    }
                  }))
                },
                success: function () {
                  e.remoteConfigInfo.isOpenProxyWxApi && e.ckObjectFullFill("custom_order") && (e.track("custom_order", {
                    is_sdk_auto_track: !0,
                    _auto_proxy_data: e.formatAutoData("custom_order"),
                    order: {
                      order_time: Number((new Date).getTime()),
                      order_status: "payed"
                    }
                  }), e.clearProxyData("custom_order"))
                },
                fail: function () {
                  e.remoteConfigInfo.isOpenProxyWxApi && e.ckObjectFullFill("custom_order") && e.track("custom_order", {
                    is_sdk_auto_track: !0,
                    _auto_proxy_data: e.formatAutoData("custom_order"),
                    order: {
                      order_time: Number((new Date).getTime()),
                      order_status: "cancel_pay"
                    }
                  })
                }
              }, this.track.bind(this))
            }, this.clearProxyData = function (e) {
              var t = this,
                i = Object.keys(this.autoProxyData[e]);
              0 !== i.length && i.forEach(function (i) {
                try {
                  t.autoProxyData[e][i]._sr_track_url = "", t.autoProxyData[e][i]._sr_track_body = ""
                } catch (e) {
                  t.track("sdk_error_log", {
                    _sdk_error_log: {
                      message: "clearProxyData error",
                      type: L,
                      error: e.message
                    }
                  }), console.log("clearProxyData error", e)
                }
              })
            }, this.ckObjectFullFill = function (e) {
              var t = this;
              if (void 0 === this.autoProxyData[e]) return !1;
              var i = Object.keys(this.autoProxyData[e]);
              if (0 === i.length) return !1;
              var n = !0;
              return i.forEach(function (i) {
                try {
                  "" == t.autoProxyData[e][i]._sr_track_body && (n = !1)
                } catch (e) {
                  t.track("sdk_error_log", {
                    _sdk_error_log: {
                      message: "ckObjectFullFill error",
                      type: L,
                      error: e.message
                    }
                  }), console.log("error ckObjectFullFill", e)
                }
              }), n
            }, this.checkRequestUrl = function (e) {
              var t = [];
              return this.needCheckUrlInfo.forEach(function (n) {
                e.includes(n.url) && t.push(i({}, n))
              }), t
            }, this.formatAutoData = function (e) {
              var t = this,
                n = i({}, this.autoProxyData[e]);
              return Object.keys(n).forEach(function (e) {
                try {
                  n[e] = d.encode(JSON.stringify(n[e]))
                } catch (e) {
                  t.track("sdk_error_log", {
                    _sdk_error_log: {
                      message: "formatAutoData error",
                      type: L,
                      error: e.message
                    }
                  }), console.log("error formatAutoData", e)
                }
              }), n
            }, this.triggerFlush = m(function () {
              e.checkAndUpload()
            }, 1e3), this.eventDataFmatter = function (t) {
              var n = +new Date,
                o = e.getPageInfo();
              if (void 0 !== e._onQueue) {
                var r = e._onQueue(t);
                g(t) ? t = r : console.warn("eventDataFmatter should return Object type")
              }
              return i(i(i({}, o), t), {
                time: n
              })
            }, this.checkRequiredOptionItem = function () {
              return !!e.option.token || (e.option.skipTokenCheck ? (console.warn("token 未配置，已跳过该检查"), !0) : (console.error("sdk.init - Option 必要参数配置缺失，请检查"), !1))
            }, this.checkVersionInfo = function () {
              if (e.setContext({
                  sr_sdk_version: e.version
                }, 1), e.isDev()) {
                var t = "https://mp.zhls.qq.com/sdk/sr-sdk-version-info.json?timesamp=" + Date.now();
                return e.request({}, {
                  url: t,
                  method: "GET"
                }).then(function (t) {
                  var i = (t.data || {})[e.name],
                    n = !0;
                  if (i) return e.version && (1 === w(i.version.min, e.version) ? (console.error("当前SDK版本过低, 请升级！"), n = !1) : 1 === w(i.version.max, e.version) && console.warn("当前SDK有更新, 推荐升级！")), {
                    success: n,
                    data: i,
                    msg: ""
                  }
                }).catch(function (e) {
                  return void 0 === e && (e = {}), {
                    success: !1,
                    data: void 0,
                    msg: e.errMsg
                  }
                })
              }
            }, this.queueInitialize = function () {
              var t = e.getServerUrl(),
                n = !0;
              return e.queue = new O({
                request: function (o) {
                  n || -1 === (null == t ? void 0 : t.indexOf(xe)) || (t = "https://zhls.qq.com/api/report?token=" + e.option.token);
                  var r = o.events.map(function (t) {
                    return i(i({}, t), {
                      from: "undefined" != typeof jd ? "sr-sdk-jd" : "undefined" != typeof tt ? "sr-sdk-bytedancemp" : "undefined" != typeof qq ? "sr-sdk-qqmp" : "undefined" != typeof swan ? "sr-sdk-baidu" : "undefined" != typeof dd ? "sr-sdk-dd" : "undefined" != typeof my ? "sr-sdk-alimp" : "sr-sdk-wxapp",
                      tracking_id: e.tracking_id,
                      log_id: ++e.log_id
                    })
                  });
                  return e.setCache(R, {
                    last_tracking_id: e.tracking_id,
                    last_max_log_id: e.log_id
                  }), e.request(r, {
                    url: t,
                    method: "POST"
                  }).catch(function (e) {
                    return console.error("APICaller error", e), "request:fail url not in domain list" === e.msg && (n = !1), e
                  })
                }
              }), !0
            }, this.trackLogEvents = function () {
              var t = e.getCache(R) || {};
              return t.last_max_log_id ? (e.track("logid_events", t), !0) : (++e.log_id, !1)
            }, this.tracking_id = y(), this.log_id = -1, this.checkStaticMethods()
          }
          return e.prototype.init = function (e) {
            if (this.inited) return this;
            var t = ke.getStorageSync("__SR_SDK_TRACKER___production"),
              i = t && t.USER_INFO && t.USER_INFO.app_id || "";
            i && i !== this.option.appid && ke.removeStorageSync("__SR_SDK_TRACKER___production"), this.version = we || "", this.option = v(this.defaultOptions, this.option, e);
            var n, o = typeof e.autoProxy;
            if ("object" === o) {
              var r = e.autoProxy,
                s = r.openAutoTrackOpenId,
                a = void 0 === s || s,
                c = r.openSdkShareDepth,
                l = void 0 === c || c,
                u = r.openAutoTrackUnionId,
                h = void 0 === u || u,
                p = r.autoTrack,
                d = void 0 !== p && p,
                g = r.page_pull_down_refresh,
                f = void 0 !== g && g;
              this.option.proxyComponent = !0, this.option.proxyPage = !0, this.option.openAutoTrackOpenId = a, this.option.openSdkShareDepth = l, this.option.autoTrack = d, this.option.openAutoTrackUnionId = h, this.option.trackApp = !0, "object" == typeof this.option.autoProxy && (this.option.autoProxy.page_pull_down_refresh = f)
            }
            if ("boolean" === o && e.autoProxy && (this.option.proxyComponent = !0, this.option.proxyPage = !0, this.option.openAutoTrackOpenId = !0, this.option.openAutoTrackUnionId = !0, this.option.autoTrack = !0, this.option.openSdkShareDepth = !0, this.option.trackApp = !0), !this.checkRequiredOptionItem()) return this;
            this.cacheManagerInitialize();
            try {
              this.proxyInitialize()
            } catch (e) {
              this.errorHandle(e)
            }
            return this.queueInitialize(), this.contextInitialize(), this.inited = !0, this.checkVersionInfo(), this.initRemoteConfig(), this.option.openProxyRequest && this.hackAutoTrack(), this.option.openErrorMonitoring && (n = this.track.bind(this), Z.onError(function (e) {
              e && n("sdk_error_log", {
                _sdk_error_log: {
                  message: "JS_RUN_ERROR",
                  type: G,
                  error: e
                }
              })
            }), Y({
              complete: function (e, t) {
                var i = e.errMsg,
                  o = e.statusCode,
                  r = e.data,
                  s = "";
                i.indexOf("timeout") > -1 ? s = "timeout" : i.indexOf("fail") > -1 ? s = "failed" : o ? o < 0 ? s = "failed" : o >= 400 && (s = "error") : s = "failed", s && n("sdk_error_log", {
                  _sdk_error_log: {
                    message: "AJAX_ERROR",
                    type: B,
                    error: {
                      AJAX_ERROR: "request " + s,
                      resStatus: o || 0,
                      resDuration: Date.now() - t.requestStartTime,
                      resData: T(r),
                      reqUrl: t.url,
                      reqMethod: t.method || "get",
                      reqParam: T(t.data),
                      errMsg: i.slice(0, 1e3)
                    }
                  }
                })
              }
            }, n)), this
          }, e.prototype.track = function (e, t) {
            if (this.remoteConfigInfo.masterSwitch) {
              var i = this.option.debug;
              JSON.stringify(t || {}).length > 5e3 && console.warn("监测到超过5000的上报日志：" + e);
              var n = this.eventDataFmatter(t);
              return i && console && "function" == typeof console.log && console.log("【Track】 " + e, n), this.queue.add({
                type: e,
                props: n
              }), this.queue.checkQueue(), (this.queue.getItems().length || 0) > 9 && this.reportState === U ? this.flush() : this.triggerFlush(), this
            }
          }, e.prototype.setContext = function (e, t, n) {
            return void 0 === t && (t = 0), void 0 === n && (n = !1), console.warn("setContext 不在推荐使用，请用更轻便的 setUser、setChan等方法代替"), n && this.flush(), void 0 !== e.sr_sdk_version && 0 === t && delete e.sr_sdk_version, this.context = i(i(i({}, this.context), e), {
              wx_user: i(i({}, this.context.wx_user), e.wx_user || {}),
              chan: i(i({}, this.context.chan), e.chan || {})
            }), this.setIdenTifier({
              value: i({}, e),
              type: "context",
              isSr: t
            }), this
          }, e.prototype.setUser = function (e, t, n) {
            return void 0 === e && (e = {}), void 0 === t && (t = 0), void 0 === n && (n = !1), n && this.flush(), this.context = Object.assign({}, this.context, {
              wx_user: i(i({}, this.context.wx_user), e)
            }), this.setIdenTifier({
              value: i({}, e),
              type: "user",
              isSr: t
            }), this.setCache(E, this.context.wx_user), this
          }, e.prototype.setChan = function (e, t, n) {
            void 0 === t && (t = 0), void 0 === n && (n = !1), n && this.flush();
            var o = e.chan_id,
              r = (this.context.chan || {}).chan_id;
            return this.context = Object.assign({}, this.context, {
              chan: i(i(i({}, this.context.chan), e), {
                chan_id: o || r || ""
              })
            }), this.setIdenTifier({
              value: i({}, e),
              type: "chan",
              isSr: t
            }), this
          }, e.prototype.setComponent = function (e) {
            var t = e.component_id,
              n = e.component_name;
            return this.context = Object.assign({}, this.context, {
              component: i(i({}, e), {
                component_id: t,
                component_name: n
              })
            }), this
          }, e.prototype.clearComponent = function () {
            return delete this.context.component, this
          }, e.prototype.setActivityInfo = function (e) {
            var t = e.activity_id,
              n = e.activity_name,
              o = e.activity_type,
              r = e.activity_index;
            return this.context = Object.assign({}, this.context, {
              activity_info: i(i({}, e), {
                activity_id: t,
                activity_name: n,
                activity_type: o,
                activity_index: r
              })
            }), this
          }, e.prototype.clearActivityInfo = function () {
            return delete this.context.activity_info, this
          }, e.prototype.startReport = function () {
            return this.reportState = U, this.triggerFlush(), this
          }, e.prototype.resumeReport = function () {
            var e = this.getCache(A) || [];
            return this.queue.unshift(e), this.reportState === j && (this.reportState = U), this.triggerFlush(), this
          }, e.prototype.pauseReport = function () {
            return this.reportState = j, this.setCache(A, this.queue.clean()), this
          }, e.prototype.flush = function () {
            return this.queue.flush(this.context, this.getCache(N)), this
          }, e.prototype.onQueue = function (e) {
            return this._onQueue = e, this
          }, e.prototype.getInfo = function () {
            var e = {
              option: this.option,
              tracking_id: this.tracking_id,
              context: this.context,
              is_dev: this.isDev()
            };
            return "SR_SDK_INFO=" + d.encode(JSON.stringify(e))
          }, e.prototype.getLocalId = function () {
            return this.context.wx_user.local_id || ""
          }, e.prototype.getWxUserInfo = function () {
            return i({}, this.context.wx_user)
          }, e.prototype.getChanInfo = function () {
            return i({}, this.context.chan)
          }, e.prototype.getPagePathInfo = function () {
            return he() || ""
          }, e.prototype.checkStaticMethods = function () {
            if ("development" === this.env) try {
              var e = this.constructor;
              ["create"].forEach(function (t) {
                !e[t] && console.error("static " + t + " should be implement")
              })
            } catch (e) {
              console.error("checkStaticMethods error", e)
            }
          }, e.prototype.checkFallback = function () {
            var e = this;
            setTimeout(function () {
              e.checkAndUpload(), e.checkFallback()
            }, 1e4)
          }, e.prototype.checkAndUpload = function () {
            this.reportState === U && this.flush()
          }, e.prototype.contextInitialize = function () {
            var e = this.getUser(),
              t = this.getSystemInfo(),
              n = t.brand,
              o = t.model,
              r = t.version,
              s = t.environment,
              a = t.screenWidth,
              c = t.screenHeight,
              l = t.system,
              u = t.platform,
              h = t.SDKVersion,
              p = t.benchmarkLevel,
              d = t.locationReducedAccuracy,
              g = this.getFrameworkInfo();
            this.context = v(this.context, {
              wx_user: i(i({}, e), {
                app_id: this.option.appid
              }),
              system_info: {
                brand: n,
                model: o,
                version: r,
                environment: s,
                screenWidth: a,
                screenHeight: c,
                system: l,
                platform: u,
                SDKVersion: h,
                benchmarkLevel: p,
                LRA: d
              },
              framework_info: g,
              chan: {}
            }), this.setIdenTifier({
              value: {
                app_id: this.option.appid
              },
              type: "user",
              isSr: 1
            })
          }, e.prototype.rleitrValue = function (e, t, i) {
            var n = e.split("");
            return n[t] = i, n.join("")
          }, e.prototype.setuserchanItr = function (e, t, i) {
            var n = this,
              o = this.getCache(N) || "-----";
            Object.keys(e).forEach(function (e, r) {
              "user" === t && -1 !== n.idenTifierUserArr.indexOf(e) && n.setCache(N, n.rleitrValue(o, n.idenTifierUserArr.indexOf(e), i)), "chan" === t && -1 !== n.idenTifierChanArr.indexOf(e) && (n.context.idenTifier = n.rleitrValue(n.context.idenTifier, n.idenTifierChanArr.indexOf(e), i))
            })
          }, e.prototype.setcontextItr = function (e, t) {
            e.wx_user && this.setuserchanItr(i({}, e.wx_user), "user", t), e.chan && this.setuserchanItr(i({}, e.chan), "chan", t), delete e.wx_user, delete e.chan, this.setuserchanItr(i({}, e), "chan", t)
          }, e.prototype.setIdenTifier = function (e) {
            var t = e.value,
              i = e.type,
              n = e.isSr;
            "context" === i ? this.setcontextItr(t, n) : this.setuserchanItr(t, i, n)
          }, e.prototype.getUser = function () {
            var e = this.context.wx_user || this.getCache(E) || {};
            return e.local_id && 50 === e.local_id.length || (e = {
              local_id: y()
            }, this.setIdenTifier({
              value: i({}, e),
              type: "user",
              isSr: 1
            }), this.setCache(E, e)), e
          }, e.prototype.cacheManagerInitialize = function () {
            var e = this.getCacheManager();
            this.cacheManager = e
          }, e.prototype.getCache = function (e) {
            return this.cacheManager ? (this.cacheManager.get(P) || {})[e] : (console.error(F.MISS), {})
          }, e.prototype.setCache = function (e, t) {
            var n;
            this.cacheManager || console.error(F.MISS);
            var o = i(i({}, this.cacheManager.get(P) || {}), ((n = {})[e] = t, n));
            this.cacheManager.set(P, o)
          }, e.prototype.getServerUrl = function () {
            return ("function" == typeof this.option.serverUrl ? this.option.serverUrl.call(this) : this.option.serverUrl || xe) + "?token=" + this.option.token
          }, e.prototype.getTrackingId = function () {
            return this.tracking_id
          }, n([se], e.prototype, "init", null), n([se, ae], e.prototype, "track", null), n([se, ae], e.prototype, "setContext", null), n([se, ae], e.prototype, "setUser", null), n([se, ae], e.prototype, "setChan", null), n([se, ae], e.prototype, "setComponent", null), n([se, ae], e.prototype, "clearComponent", null), n([se, ae], e.prototype, "setActivityInfo", null), n([se, ae], e.prototype, "clearActivityInfo", null), n([se, ae], e.prototype, "startReport", null), n([se, ae], e.prototype, "resumeReport", null), n([se, ae], e.prototype, "pauseReport", null), n([se, ae], e.prototype, "flush", null), n([se, ae], e.prototype, "onQueue", null), n([se, ae], e.prototype, "getInfo", null), n([se, ae], e.prototype, "getLocalId", null), n([se, ae], e.prototype, "getWxUserInfo", null), n([se, ae], e.prototype, "getChanInfo", null), n([se, ae], e.prototype, "getPagePathInfo", null), e
        }();

        function Ie(e, t, i, n) {
          void 0 === n && (n = !1);
          var r = e[t];
          e[t] = function () {
            for (var e = arguments, t = this, s = [], a = 0; a < arguments.length; a++) s[a] = e[a];
            var c = function () {
              return r && r.apply(t, s)
            };
            return n && (c = function () {
              return Promise.resolve().then(function () {
                return r.apply(t, s)
              })
            }), i.apply(this, o([c], s))
          }
        }
        for (var Ce = function () {}, Oe = {}, Pe = {}, Ae = function () {
            return (new Date).getTime()
          }, Ee = function (e, t, i, n, o, r) {
            return function (s) {
              return function (e, t, i, n, o, r, s) {
                if (Ie(e, "onLoad", function (e, t) {
                    e(), this.lauchTime = Ae()
                  }), ve(s, "browse_page") && Ie(e, "onShow", function (e) {
                    var n = this,
                      o = function () {
                        var e = _e(n);
                        n.showTime = Ae();
                        var o = pe.call(n, "room_id") || pe.call(n, "roomId") || pe.call(n, "roomid");
                        o && i({
                          room_id: o
                        }, 1), t("browse_wxapp_page", {
                          is_sdk_auto_track: !0,
                          refer_page: be(Pe),
                          is_newly_open: !Oe[e]
                        }), Oe[e] = !0
                      };
                    e().then(o).catch(o)
                  }, !0), ve(s, "leave_page") && Ie(e, "onHide", function (e) {
                    e();
                    var i = this.showTime ? Ae() - this.showTime : 0;
                    i = i > 144e5 ? 0 : i, this.showTime = 0, t("leave_wxapp_page", {
                      is_sdk_auto_track: !0,
                      refer_page: be(Pe),
                      stay_time: i
                    }), Pe = this, n({
                      refer_page: _e(this)
                    })
                  }), ve(s, "leave_page") && Ie(e, "onUnload", function (e) {
                    e();
                    var i = this.showTime ? Ae() - this.showTime : 0;
                    i = i > 144e5 ? 0 : i, t("leave_wxapp_page", {
                      is_sdk_auto_track: !0,
                      refer_page: be(Pe),
                      stay_time: i
                    }), Pe = this, n({
                      refer_page: _e(this)
                    })
                  }), ve(s, "page_pull_down_refresh") && Ie(e, "onPullDownRefresh", function (e) {
                    e(), t("page_pull_down_refresh", {
                      is_sdk_auto_track: !0
                    })
                  }), ve(s, "page_reach_bottom") && Ie(e, "onReachBottom", function (e) {
                    e(), t("page_reach_bottom", {
                      is_sdk_auto_track: !0
                    })
                  }), ve(s, "page_share_app_message")) {
                  if ("function" == typeof e.onShareAppMessage) {
                    var a = e.onShareAppMessage || Ce;
                    e.onShareAppMessage = function (e) {
                      void 0 === e && (e = {});
                      var i = a.call(this, e) || {};
                      try {
                        var n = i.path || he.call(this, "share"); - 1 === n.indexOf("?") ? n += "?" : "&" !== n.slice(-1) && (n += "&");
                        var o = void 0,
                          s = void 0;
                        r && (o = me(), s = JSON.parse(o), n = n + "txsrShareInfoSdk=" + encodeURIComponent(o)), t("page_share_app_message", {
                          is_sdk_auto_track: !0,
                          from_type: e.from || "未知",
                          share_to: ye(e.shareTarget),
                          share_path: n,
                          share_title: i.title,
                          share_image_url: i.imageUrl,
                          refer_page: be(Pe),
                          txsr_share_info_sdk: s
                        }), i.path = n
                      } catch (e) {
                        console.error("onShareAppMessage error", e)
                      }
                      return i
                    }
                  }
                  if ("function" == typeof e.onShareTimeline) {
                    var c = e.onShareTimeline || Ce;
                    e.onShareTimeline = function (e) {
                      void 0 === e && (e = {});
                      var i = c.call(this, e) || {};
                      try {
                        var n = i.path || he.call(this, "share"),
                          o = i.query || ""; - 1 === n.indexOf("?") ? n += "?" : "&" !== n.slice(-1) && (n += "&");
                        var s = void 0,
                          a = void 0;
                        r && (s = me(), a = JSON.parse(s), n = n + "txsrShareInfoSdk=" + encodeURIComponent(s)), t("page_share_app_message", {
                          is_sdk_auto_track: !0,
                          from_type: e.from || "未知",
                          share_to: "timeline",
                          query: o,
                          share_path: n,
                          share_title: i.title,
                          share_image_url: i.imageUrl,
                          refer_page: be(Pe),
                          txsr_share_info_sdk: a
                        }), i.path = n
                      } catch (e) {
                        console.error("onShareAppMessage error", e)
                      }
                      return i
                    }
                  }
                }
                return o && Object.entries(e).filter(function (e) {
                  var t = e[0];
                  return e[1], !["onLoad", "onShow", "onReady", "onHide", "onUnload", "onPullDownRefresh", "onReachBottom", "onPageScroll", "onShareAppMessage", "onResize", "onTabItemTap"].includes(t)
                }).forEach(function (i) {
                  var n = i[0];
                  "function" == typeof i[1] && Ie(e, n, function (e) {
                    for (var i = arguments, o = [], r = 1; r < arguments.length; r++) o[r - 1] = i[r];
                    return fe.call(this, o, t, n), e()
                  })
                }), e
              }(s, e, t, i, n, o, r)
            }
          }, Re = function () {}, Ne = {}, De = {}, qe = function () {
            return (new Date).getTime()
          }, Me = function (e, t, i, n, o, r) {
            return function (s) {
              return function (e, t, i, n, o, r, s) {
                try {
                  if (e.methods = e.methods || {}, Ie(e.methods, "onLoad", function (e, t) {
                      e(), this.lauchTime = qe()
                    }), ve(s, "browse_page") && Ie(e.methods, "onShow", function (e) {
                      var n = this,
                        o = function () {
                          var e = _e(n);
                          n.showTime = qe();
                          var o = pe.call(n, "room_id") || pe.call(n, "roomId") || pe.call(n, "roomid");
                          o && i({
                            room_id: o
                          }, 1), t("browse_wxapp_page", {
                            is_sdk_auto_track: !0,
                            refer_page: be(De),
                            is_newly_open: !Ne[e]
                          }), Ne[e] = !0
                        };
                      e().then(o).catch(o)
                    }, !0), ve(s, "leave_page") && Ie(e.methods, "onUnload", function (e) {
                      e();
                      var i = this.showTime ? qe() - this.showTime : 0;
                      i = i > 144e5 ? 0 : i, t("leave_wxapp_page", {
                        is_sdk_auto_track: !0,
                        refer_page: be(De),
                        stay_time: i
                      }), De = this, n({
                        refer_page: _e(this)
                      })
                    }), ve(s, "page_pull_down_refresh") && Ie(e.methods, "onPullDownRefresh", function (e) {
                      e(), t("page_pull_down_refresh", {
                        is_sdk_auto_track: !0
                      })
                    }), ve(s, "page_reach_bottom") && Ie(e.methods, "onReachBottom", function (e) {
                      e(), t("page_reach_bottom", {
                        is_sdk_auto_track: !0
                      })
                    }), ve(s, "leave_page") && Ie(e.methods, "onHide", function (e) {
                      e();
                      var i = this.showTime ? qe() - this.showTime : 0;
                      i = i > 144e5 ? 0 : i, this.showTime = 0, t("leave_wxapp_page", {
                        is_sdk_auto_track: !0,
                        refer_page: be(De),
                        stay_time: i
                      }), De = this, n({
                        refer_page: _e(this)
                      })
                    }), ve(s, "page_share_app_message")) {
                    if ("function" == typeof e.methods.onShareAppMessage) {
                      var a = e.methods.onShareAppMessage || Re;
                      e.methods.onShareAppMessage = function (e) {
                        void 0 === e && (e = {});
                        var i = a.call(this, e) || {};
                        try {
                          var n = i.path || he.call(this, "share"); - 1 === n.indexOf("?") ? n += "?" : "&" !== n.slice(-1) && (n += "&");
                          var o = void 0,
                            s = void 0;
                          r && (o = me(), s = JSON.parse(o), n = n + "txsrShareInfoSdk=" + encodeURIComponent(o)), t("page_share_app_message", {
                            is_sdk_auto_track: !0,
                            from_type: e.from || "未知",
                            share_to: "friends",
                            share_path: n,
                            share_title: i.title,
                            share_image_url: i.imageUrl,
                            refer_page: be(De),
                            txsr_share_info_sdk: s
                          }), i.path = n
                        } catch (e) {
                          console.error("onShareAppMessage error", e)
                        }
                        return i
                      }
                    }
                    if ("function" == typeof e.methods.onShareTimeline) {
                      var c = e.methods.onShareTimeline || Re;
                      e.methods.onShareTimeline = function (e) {
                        void 0 === e && (e = {});
                        var i = c.call(this, e) || {};
                        try {
                          var n = i.path || he.call(this, "share"),
                            o = i.query || ""; - 1 === n.indexOf("?") ? n += "?" : "&" !== n.slice(-1) && (n += "&");
                          var s = void 0,
                            a = void 0;
                          r && (s = me(), a = JSON.parse(s), n = n + "txsrShareInfoSdk=" + encodeURIComponent(s)), t("page_share_app_message", {
                            is_sdk_auto_track: !0,
                            from_type: e.from || "未知",
                            share_to: ye(e.shareTarget),
                            share_path: n,
                            query: o,
                            share_title: i.title,
                            share_image_url: i.imageUrl,
                            refer_page: be(De),
                            txsr_share_info_sdk: a
                          }), i.path = n
                        } catch (e) {
                          console.error("onShareAppMessage error", e)
                        }
                        return i
                      }
                    }
                  }
                  e.methods && o && Object.entries(e.methods).filter(function (e) {
                    var t = e[0];
                    return e[1], !["onLoad", "onShow", "onReady", "onHide", "onUnload", "onPullDownRefresh", "onReachBottom", "onPageScroll", "onShareAppMessage", "onResize", "onTabItemTap", "observer"].includes(t)
                  }).forEach(function (i) {
                    var n = i[0];
                    "function" == typeof i[1] && Ie(e.methods, n, function (e) {
                      for (var i = arguments, o = [], r = 1; r < arguments.length; r++) o[r - 1] = i[r];
                      return fe.call(this, o, t, n), e()
                    })
                  })
                } catch (e) {
                  console.error("componentProxy error", e)
                }
                return e
              }(s, e, t, i, n, o, r)
            }
          }, Ue = ["utf8", "utf-8", "unicode-1-1-utf-8"], je = new Uint8Array(256), Fe = 0; Fe < je.length; ++Fe) je[Fe] = Fe;
        var Le = new function (e) {
          if (Ue.indexOf(e) < 0 && void 0 !== e && null != e) throw new RangeError("Invalid encoding type. Only utf-8 is supported");
          this.encoding = "utf-8", this.encode = function (e) {
            if ("string" != typeof e) throw new TypeError("passed argument must be of tye string");
            for (var t = unescape(encodeURIComponent(e)), i = new Uint8Array(t.length), n = t.split(""), o = 0; o < n.length; o++) i[o] = n[o].charCodeAt(0);
            return i
          }
        }("utf-8");

        function Ge() {}
        Ge.prototype.encrypt = function (e, t) {
          return function (e, t) {
            for (var i, n = e.length, o = new Uint8Array(n), r = 0, s = 0, a = 0; a < n; ++a) s = s + t[r = r + 1 & 255] & 255, i = t[r], t[r] = t[s], t[s] = i, o[a] = e[a] ^ t[t[r] + t[s] & 255];
            return o
          }(Le.encode(e), function (e) {
            for (var t = new Uint8Array(256), i = 0; i < 256; ++i) t[i] = i;
            var n, o = 0;
            for (i = 0; i < 256; ++i) o = o + t[i] + e[i % e.length] & 255, n = t[i], t[i] = t[o], t[o] = n;
            return t
          }(Le.encode(t)))
        };
        var Be = new Ge,
          He = {},
          We = function (e) {
            return e
          },
          Ve = I(),
          ze = C(),
          Ke = function (e) {
            function n() {
              var t = e.call(this) || this;
              return t.name = "mp", t.component = We, t.page = We, t.proxySetNavigation = function () {
                try {
                  var e = Ve.setNavigationBarTitle;
                  Object.defineProperty(Ve, "setNavigationBarTitle", {
                    get: function () {
                      return function (t) {
                        void 0 === t && (t = {});
                        try {
                          var i = ue();
                          try {
                            __wxConfig.page = __wxConfig.page || {}
                          } catch (e) {
                            console.error(e)
                          }
                          var n = __wxConfig.page[i.route + ".html"];
                          n && ((n.window || {}).navigationBarTitleText = t.title)
                        } catch (e) {}
                        e.call(this, t)
                      }
                    }
                  })
                } catch (e) {
                  console.warn("proxySetNavigation failed", e)
                }
              }, t.request = function (e, i) {
                try {
                  var n = function (e) {
                    return void 0 === e && (e = {}), 0 === e.code
                  };
                  "function" == typeof t.option.onUploaded && (n = t.option.onUploaded);
                  var o = {},
                    r = {};
                  if (t.option.encrypt) {
                    var s = y(),
                      a = Be.encrypt(JSON.stringify(e), s);
                    r = {
                      "Content-Type": "application/x-sr-encrypted",
                      "Content-Encrypting-Key": s
                    }, o = h.uint8ArrayToBase64(a)
                  } else o = e;
                  return new Promise(function (e, t) {
                    ze({
                      url: i.url,
                      method: i.method || "POST",
                      data: o,
                      header: r,
                      success: function (t) {
                        void 0 === t && (t = {});
                        var i = t.data,
                          o = void 0 === i ? {} : i,
                          r = n(o);
                        e({
                          success: void 0 === r || r,
                          data: o.data || o,
                          msg: o.errMsg
                        })
                      },
                      fail: function (e) {
                        t({
                          success: !1,
                          data: void 0,
                          msg: e.errMsg
                        })
                      }
                    })
                  })
                } catch (e) {
                  console.log("sdk request error", e)
                }
              }, t.defaultOptions = {
                autoProxy: !0,
                autoStart: !0,
                debug: !1,
                encrypt: !1,
                usePlugin: !1,
                proxyPage: !1,
                proxyComponent: !1,
                autoTrack: !1,
                trackApp: !0,
                openSdkShareDepth: !1,
                installFrom: "",
                openAutoTrackOpenId: !1,
                openAutoTrackUnionId: !1,
                openErrorMonitoring: !1,
                openProxyRequest: !1
              }, t.proxySetNavigation(), t
            }
            return t(n, e), n.prototype.getCacheManager = function () {
              var e = "" + this.env,
                t = function (t) {
                  return t + "_" + e
                };
              return {
                get: function (e) {
                  var i;
                  try {
                    i = "undefined" != typeof my ? Ve.getStorageSync({
                      key: t(e)
                    }).data : Ve.getStorageSync(t(e))
                  } catch (e) {
                    return console.error("CacheManager.get error", e), i
                  }
                  return i
                },
                set: function (e, i) {
                  try {
                    "undefined" != typeof my ? Ve.setStorageSync({
                      key: t(e),
                      data: i
                    }) : Ve.setStorageSync(t(e), i)
                  } catch (e) {
                    return console.error("CacheManager.set error", e), !1
                  }
                  return !0
                }
              }
            }, n.prototype.proxyInitialize = function () {
              return Ke.options = this.option, this.trackApp(), !0
            }, n.prototype.trackApp = function () {
              var e = this,
                t = !1;
              Ve.onAppShow(function (n) {
                void 0 === n && (n = {});
                var o = n,
                  r = o.query,
                  s = void 0 === r ? {} : r,
                  a = o.path,
                  c = o.shareTicket,
                  l = e.option.openSdkShareDepth,
                  u = e.option.openAutoTrackOpenId,
                  h = e.option.openAutoTrackUnionId,
                  p = e.option.appid,
                  d = function (e) {
                    void 0 === e && (e = {});
                    var t = {};
                    if ("undefined" != typeof tt && Object.keys(e).includes("[object Object]") && delete e["[object Object]"], e.scene) {
                      try {
                        var n = decodeURIComponent(e.scene);
                        (n = n.replace("?", "").trim()).split("&").map(function (e) {
                          if (e) {
                            var i = e.split("="),
                              n = i[0],
                              o = i[1];
                            _(n) && (t[n] = void 0 === o || o)
                          }
                        })
                      } catch (e) {
                        console.error(e)
                      }
                      e = i(i({}, e), t)
                    }
                    return e
                  }(s || {}),
                  g = d.txsrShareInfoSdk || "{}",
                  f = e;
                if (d && "{}" !== JSON.stringify(d)) {
                  var m = "?";
                  Object.entries(d).forEach(function (e, t) {
                    var i = e[0],
                      n = e[1];
                    m += (0 === t ? "" : "&") + i + "=" + n
                  }), a += m
                }
                var y = e.cacheManager.get(D) || "",
                  v = e.cacheManager.get(q) || "";
                if ((null == d ? void 0 : d.gdt_vid) && (y = null == d ? void 0 : d.gdt_vid, e.cacheManager.set(D, null == d ? void 0 : d.gdt_vid)), (null == d ? void 0 : d.qz_gdt) && (v = null == d ? void 0 : d.qz_gdt, e.cacheManager.set(q, null == d ? void 0 : d.qz_gdt)), e.setChan(i(i({}, d), {
                    chan_wxapp_scene: n.scene,
                    chan_refer_app_id: (n.referrerInfo || {}).appId,
                    gdt_vid: y,
                    qz_gdt: v
                  }), 1), d.chan_id && e.setChan({
                    chan_id: d.chan_id
                  }, 1), l && "{}" !== g) try {
                  e.setUser({
                    txsr_from_share_info: JSON.parse(decodeURIComponent(g))
                  }, 1)
                } catch (e) {}
                t || (t = !0, e.option.trackApp && ve(e.option.autoProxy, "app_launch") && e.track("app_launch", {
                  is_sdk_auto_track: !0,
                  page: a
                }));
                var b = (e.cacheManager.get(P) || {}).USER_INFO || {},
                  k = b.open_id,
                  S = void 0 === k ? "" : k,
                  x = b.union_id;
                if (u && !S || h && (void 0 === x || !x)) try {
                  Ve.login({
                    success: function (e) {
                      var t = e.code;
                      ze({
                        url: "https://zhls.qq.com/wxlogin/getOpenId?appid=" + p + "&js_code=" + t,
                        data: {},
                        header: {
                          "content-type": "application/json"
                        },
                        success: function (e) {
                          var t = e.data,
                            i = t.openId,
                            n = t.unionId,
                            o = void 0 === n ? "" : n;
                          f.setUser({
                            open_id: i,
                            union_id: o
                          }, 1), l && c && i && f.getOpenGId(c, i)
                        }
                      })
                    }
                  })
                } catch (t) {
                  e.errorHandle(t)
                }
                l && c && S && e.getOpenGId(c, S), e.option.trackApp && ve(e.option.autoProxy, "app_show") && e.track("app_show", {
                  is_sdk_auto_track: !0,
                  page: a
                })
              }), Ve.onAppHide(function () {
                e.option.trackApp && ve(e.option.autoProxy, "app_exit") && e.track("exit_wxapp", {
                  is_sdk_auto_track: !0
                })
              })
            }, n.prototype.getOpenGId = function (e, t) {
              var i = this.option.appid,
                n = this;
              Ve.getShareInfo({
                shareTicket: e,
                success: function (e) {
                  var o = e.iv,
                    r = e.encryptedData;
                  ze({
                    url: "https://zhls.qq.com/wxlogin/convertData",
                    data: {
                      appid: i,
                      openid: t,
                      data: r,
                      iv: o
                    },
                    header: {
                      "content-type": "application/json"
                    },
                    success: function (e) {
                      var t = (e && e.data).openGId;
                      t && n.setChan({
                        openGId: t
                      }, 1)
                    }
                  })
                },
                fail: function (e) {}
              })
            }, n.prototype.errorHandle = function (e) {
              try {
                var t = this.getServerUrl();
                this.request({
                  type: "sdk api exec error",
                  props: {
                    sr_sdk_version: this.version,
                    system_info: this.getSystemInfo(),
                    framework_info: this.getFrameworkInfo(),
                    message: e,
                    stack: e
                  }
                }, {
                  url: t,
                  method: "POST"
                })
              } catch (e) {
                console.log("errorHandle error", e)
              }
            }, n.prototype.getSystemInfo = function () {
              try {
                return Ve.getSystemInfoSync()
              } catch (e) {
                return {}
              }
            }, n.prototype.getFrameworkInfo = function () {
              var e, t;
              try {
                if (process && {
                    NODE_ENV: "production",
                    BASE_URL: "/"
                  } && {
                    NODE_ENV: "production",
                    BASE_URL: "/"
                  }.TARO_ENV && (e = "taro"), this.option.installFrom) {
                  var i = String(this.option.installFrom).toLowerCase(),
                    n = /^((taro)|(uni[\-]?app)|(chameleon)|(wepy)|(mpvue))(@v?([\S]*))?/g.exec(i);
                  n && n[1] && ("taro" === e && n[2] ? t = n[8] : "taro" !== e && (t = n[8], e = n[3] ? "uni-app" : n[4] || n[5] || n[6] || "unknown"))
                }
              } catch (t) {
                e = "unknown"
              }
              return {
                framework: e,
                version: t
              }
            }, n.prototype.getPageInfo = function () {
              var e = he(),
                t = ue() || {},
                i = de,
                n = (t.data || {}).title || t.title;
              try {
                void 0 === n && e && !He[e] && (He[e] = !0, console.warn("页面[" + e + "]没有实现 title 属性，会导致部分机型下收集不到页面标题!")), "string" == typeof n && (i = function () {
                  return n
                }), "function" == typeof n && (i = n)
              } catch (e) {
                console.error("curPage.data.title 执行错误", e)
              }
              return {
                page: e,
                page_title: i()
              }
            }, n.prototype.isDev = function () {
              return ge()
            }, n.create = function () {
              var e;
              try {
                e = new n
              } catch (t) {
                e = n.prototype, console.error("new sr_sdk failed", t)
              }
              return e
            }, n
          }(Te).create(),
          Qe = Page,
          Je = Component;
        return Page = function (e) {
          if (Ke.option.proxyPage) {
            var t = Ee(Ke.track.bind(Ke), Ke.setChan.bind(Ke), Ke.setContext.bind(Ke), Ke.option.autoTrack, Ke.option.openSdkShareDepth, Ke.option.autoProxy);
            Qe(t(e))
          } else Qe(e)
        }, Page.after = Qe.after, Component = function (e) {
          if (Ke.option.proxyComponent) {
            var t = Me(Ke.track.bind(Ke), Ke.setChan.bind(Ke), Ke.setContext.bind(Ke), Ke.option.autoTrack, Ke.option.openSdkShareDepth, Ke.option.autoProxy);
            return Je(t(e))
          }
          return Je(e)
        }, Component.after = Je.after, Ke
      }()
    },
    191: function (e, t, i) {
      var n;
      ! function (t) {
        "use strict";

        function o() {}
        var r = o.prototype,
          s = t.EventEmitter;

        function a(e, t) {
          for (var i = e.length; i--;)
            if (e[i].listener === t) return i;
          return -1
        }

        function c(e) {
          return function () {
            return this[e].apply(this, arguments)
          }
        }

        function l(e) {
          return "function" == typeof e || e instanceof RegExp || !(!e || "object" != typeof e) && l(e.listener)
        }
        r.getListeners = function (e) {
          var t, i, n = this._getEvents();
          if (e instanceof RegExp)
            for (i in t = {}, n) n.hasOwnProperty(i) && e.test(i) && (t[i] = n[i]);
          else t = n[e] || (n[e] = []);
          return t
        }, r.flattenListeners = function (e) {
          var t, i = [];
          for (t = 0; t < e.length; t += 1) i.push(e[t].listener);
          return i
        }, r.getListenersAsObject = function (e) {
          var t, i = this.getListeners(e);
          return i instanceof Array && ((t = {})[e] = i), t || i
        }, r.addListener = function (e, t) {
          if (!l(t)) throw new TypeError("listener must be a function");
          var i, n = this.getListenersAsObject(e),
            o = "object" == typeof t;
          for (i in n) n.hasOwnProperty(i) && -1 === a(n[i], t) && n[i].push(o ? t : {
            listener: t,
            once: !1
          });
          return this
        }, r.on = c("addListener"), r.addOnceListener = function (e, t) {
          return this.addListener(e, {
            listener: t,
            once: !0
          })
        }, r.once = c("addOnceListener"), r.defineEvent = function (e) {
          return this.getListeners(e), this
        }, r.defineEvents = function (e) {
          for (var t = 0; t < e.length; t += 1) this.defineEvent(e[t]);
          return this
        }, r.removeListener = function (e, t) {
          var i, n, o = this.getListenersAsObject(e);
          for (n in o) o.hasOwnProperty(n) && -1 !== (i = a(o[n], t)) && o[n].splice(i, 1);
          return this
        }, r.off = c("removeListener"), r.addListeners = function (e, t) {
          return this.manipulateListeners(!1, e, t)
        }, r.removeListeners = function (e, t) {
          return this.manipulateListeners(!0, e, t)
        }, r.manipulateListeners = function (e, t, i) {
          var n, o, r = e ? this.removeListener : this.addListener,
            s = e ? this.removeListeners : this.addListeners;
          if ("object" != typeof t || t instanceof RegExp)
            for (n = i.length; n--;) r.call(this, t, i[n]);
          else
            for (n in t) t.hasOwnProperty(n) && (o = t[n]) && ("function" == typeof o ? r.call(this, n, o) : s.call(this, n, o));
          return this
        }, r.removeEvent = function (e) {
          var t, i = typeof e,
            n = this._getEvents();
          if ("string" === i) delete n[e];
          else if (e instanceof RegExp)
            for (t in n) n.hasOwnProperty(t) && e.test(t) && delete n[t];
          else delete this._events;
          return this
        }, r.removeAllListeners = c("removeEvent"), r.emitEvent = function (e, t) {
          var i, n, o, r, s = this.getListenersAsObject(e);
          for (r in s)
            if (s.hasOwnProperty(r))
              for (i = s[r].slice(0), o = 0; o < i.length; o++) !0 === (n = i[o]).once && this.removeListener(e, n.listener), n.listener.apply(this, t || []) === this._getOnceReturnValue() && this.removeListener(e, n.listener);
          return this
        }, r.trigger = c("emitEvent"), r.emit = function (e) {
          var t = Array.prototype.slice.call(arguments, 1);
          return this.emitEvent(e, t)
        }, r.setOnceReturnValue = function (e) {
          return this._onceReturnValue = e, this
        }, r._getOnceReturnValue = function () {
          return !this.hasOwnProperty("_onceReturnValue") || this._onceReturnValue
        }, r._getEvents = function () {
          return this._events || (this._events = {})
        }, o.noConflict = function () {
          return t.EventEmitter = s, o
        }, void 0 === (n = function () {
          return o
        }.call(t, i, t, e)) || (e.exports = n)
      }("undefined" != typeof window ? window : this || {})
    },
    192: function (e, t, i) {
      var n;

      function o(e, t) {
        return new RegExp(e, t)
      }

      function r(e) {
        return Array.isArray(e)
      }

      function s(e) {
        return null !== e && "object" == typeof e
      }

      function a(e) {
        return null != e
      }
      n = {
        "zh-CN": {
          authorization: {
            revokeProtocol: "撤销协议",
            revokeProtocolTip: "撤销后，您的账号会退出仅提供浏览服务，是否确定撤销？",
            ihaveRead: "本人已阅读及了解",
            contentAndAgree: "的內容，并同意本公司合理使用您的个人资料。",
            loginWithPhone: "使用手机号登录",
            locationEnabledTip: "系统定位服务未开启",
            locationAuthorizedTip: "您尚未对该小程序进行位置授权",
            alreadyRegister: "当前手机号已注册会员了",
            etcContent: "等内容",
            joinEnjoy: "加入后享专属活动&会员好礼",
            membershipAgreement: "会员协议",
            authorizationLogin: "授权登录",
            onKeyLoginWithPhone: "手机号一键登录",
            pleaseReadAndAgree: "请阅读并同意",
            privacyPolicy: "隐私条款",
            requestAuthorizationDesc: "允许我们在必要场景下，合理使用您的个人信息，且阅读 并同意",
            skipTemporarily: "暂时跳过",
            welcomeJoin: "欢迎加入",
            obtainVerificationCode: "获取验证码",
            resend: "{n}s",
            verificationCodeSentSuccess: "验证码发送成功",
            PleaseEnterPhone: "请输入手机号",
            PleaseEnterCorrectPhone: "请输入正确的手机号",
            PleaseEnterVerificationCode: "请输入验证码",
            toLoginTip: "您暂时没有登录，去登录",
            toLogin: "去登录",
            seeNum: "查看数字",
            hideNum: "隐藏数字",
            memberUpdateTip: "{n}秒后自动更新，请在店内消费使用",
            useWxPay: "使用微信支付",
            useAliPay: "使用支付宝支付",
            SelectRegion: "选择地区"
          },
          businessWechat: {
            authFailTip: "用户信息授权失败",
            getPluginConfigFailTip: "获取插件配置信息失败",
            groupIsDismissedTip: "群聊已解散",
            groupIsFullTip: "群聊已满员",
            inviteSuccessTip: "客服邀请已发出，请返回聊天框查看添加呦～",
            isAlreadyFriendTip: "发送的客服人员已经和当前用户是好友关系，请返回聊天框查看呦～",
            noCustomerServiceTip: "当前配置没有客服人员",
            sendMsgFailTip: "消息发送失败",
            userAlreadyInGroupAndGroupIsFullTip: "用户已经加入群聊且群聊已满员",
            userAlreadyInGroupTip: "用户已经加入群聊",
            userInBlackListTip: "用户命中企业群聊黑名单"
          },
          global: {
            simpleChinese: "简体中文",
            traditionalChinese: "繁体中文",
            english: "英文",
            tryLoading: "玩命加载中...",
            congestionTip: "亲，活动太火爆了，可以稍后再试试哈",
            tryAgain: "现在试试",
            submit: "提交",
            updateNotice: "更新提示",
            updateNoticeTip: "新版本已经准备好，请重启应用！",
            orderListEmptyTip: "您暂时还没有订单哦~",
            reserveList: "哎呀，您还没有预约哦~",
            storedValue: "哎呀，您还没有储值哦~",
            redbag: "哎呀，您还没有红包哦~",
            coupons: "您暂时没有优惠券，快去领取吧！",
            noService: "暂未开放小程序点单服务，敬请期待~",
            nearbyStores: "您所在的位置暂无门店，敬请期待",
            noGoods: "当前门店暂无可售商品，请切换门店或联系商家",
            address: "您暂时还没有地址哦~",
            favoriteStores: "暂无收藏门店~",
            groupWork: "暂无限时拼团活动，敬请期待哦~",
            giftCard: "哎呀，您还没有礼品卡哦~",
            getCoupons: "当前暂无优惠券可以领取哦",
            getPointsMall: "当前暂无积分商品可兑换，敬请期待",
            comma: ",",
            colon: "：",
            period: "。",
            semicolon: "；",
            tip: "提示",
            confirm: "确定",
            cancel: "取消",
            iknow: "我知道了",
            thinkAgain: "再想想",
            deleteSuccess: "删除成功",
            clearCache: "清除缓存",
            confirmCancelOrder: "确定要清除缓存？",
            chineseMainland: "中国大陆",
            hongkong: "中国香港",
            macau: "中国澳门",
            singapore: "新加坡",
            philippines: "菲律宾",
            malaysia: "马来西亚",
            scoreLevelOne: "非常差",
            scoreLevelTwo: "较差",
            scoreLevelThree: "一般",
            scoreLevelFour: "满意",
            scoreLevelFive: "超赞",
            point: "分",
            no: "否",
            yes: "是",
            ok: "好的",
            noReservationTimesAvailable: "目前暂无可供预约的时间",
            homePage: "首页",
            systemBusyPleaseTryAgainLater: "业务繁忙，请稍后重试",
            highTrafficPpleaseRefreshAndRetry: "访问人数较多，请刷新后再试",
            benefitClaimLimitReached: "您领取福利次数已达上限啦",
            eventTooBusyPleaseRetry: "活动太火爆了，请重试~",
            receive: "领取",
            Score: "分数",
            or: "或",
            password: "密码",
            QRCode: "二维码",
            Nationwide: "全国",
            PrivacyCall: "安全呼叫",
            PrivacyCallTips: "使用加密拨号，若呼叫异常，尝试切换本机呼叫，为保证服务质量通话可能会被录音。",
            PrivacyCallBtnTip: "隐私号码呼叫，保障信息安全",
            Call: "本机呼叫",
            PrivacyProtocol: "隐私协议",
            AccountAuthMobile: "账户授权号码",
            ServiceIntro: "服务介绍"
          },
          order: {
            returnBalance: "返余额",
            removeHiddenGoodsTips: "【{n}】与其他优惠不可同享，该券取消后将删除特定商品【{m}】！",
            removeHiddenGoodsTipsNoInfo: "优惠券与其他优惠不可同享，优惠券取消后将删除特定商品！",
            removeHiddenGoodsAgainOrder: "请重新点单！",
            Gotit: "知道了",
            needDiscount: "我要优惠",
            doNotRemindNextTime: "下次不再提醒",
            warmReminder: "溫馨提示",
            starReminderWordsBefore: "放弃本单促销优惠，可额外多获得",
            starReminderWordsAfter: "确认放弃促销优惠吗？",
            pleaseModifyApproach: "请修改做法",
            limitBuyBefore: "限购",
            limitSelectBefore: "最多",
            limitBuyAfter: "件",
            saveSuccess: "保存成功",
            pleaseSelectSpecification: "请选择规格",
            confirmAbandonAllAddOns: "确定放弃所有已加购商品？",
            saveChanges: "去保存",
            continue: "继续",
            unsavedChangesPrompt: "存在商品修改未保存，是否继续操作？",
            pleaseSelectAddOnItems: "请选择加购商品",
            oneItemAddedToCart: "一键加购",
            abandonAddToCart: "放弃加购",
            maxAddToCart: "最多加购",
            addedToCart: "已加购",
            quantity: "数量",
            pleaseModify: "请修改",
            callTheStore: "致电门店",
            checkOrder: "查看订单",
            anyQuestion: "若有疑问可咨询门店人员或查看订单",
            payError: "订单支付异常",
            waitPatiently: "请耐心等待",
            payResultGetting: "订单支付结果获取中",
            queueCouponTip: "抱歉，等待的优先订单过多，可能会超出{m}分钟，请问仍然使用优先劵吗？",
            noOrderTip: "未查看到订单号，请登录后重试",
            deleteTip: "确认删除订单吗？删除后，订单将无法恢复",
            servivePhone: "客服电话",
            confirmCancel: "确认撤销",
            cancelRefundTip1: "撤销退款中，请稍后",
            cancelRefundTip2: "撤销后，将无法再次申请退款",
            cancelRefundTip3: "退款单已撤销",
            shopAuditing: "商家审核中",
            shopHasRefund: "商家已退款",
            shopHasRefuse: "商家已拒绝",
            userHasCancel: "用户撤销退款",
            refundDesc1: "用户提交了商品退款请求，商家正在处理您的退款，按支付方式原路返还",
            refundDesc2: "商家审核中，待商家确认审核通过，按支付方式原路返还，如有疑问请联系我们",
            refundDesc3: "商家已处理您的退款，按支付方式原路返还，将在1-7个工作日到账，如有疑问请联系我们",
            refundDesc4: "商家已拒绝您的退款",
            refundDesc5: "用户撤销了退款申请，如需再次申请退款请联系商家操作",
            ifHasQuestion: "，如有疑问请",
            contactShop: "联系门店",
            contactUs: "联系我们",
            refundTime: "退款时间",
            seeVouchers: "查看凭证",
            refundReason: "退款原因",
            seeAll: "查看全部",
            refundDetail: "退款明细",
            seeRefuseReason: "查看拒绝原因",
            refuseReason: "拒绝原因",
            cancelRefund: "撤销退款",
            refundProcess: "退款进度",
            refundAmount: "退款合计",
            refundId: "退款编号",
            refundMoney: "退款金额",
            currentOrder: "今日订单",
            historyOrder: "历史订单",
            goPay: "去支付",
            payNow: "立即支付",
            orderPaymentSuccessful: "订单支付成功",
            delete: "删除",
            copyDownloadLink: "复制下载链接",
            copyDownloadLinkSuccesTip: "链接复制成功后，将链接放入浏览器完成下载",
            cancel: "取消",
            copy: "复制",
            takeOrderCode: "取单码",
            takeOrderCodeTip: "请至自提门店出示取单码取单",
            apply: "申请",
            initiatePaymentTip: "发起微信群收款需要授权以下信息",
            pinGroupUserInfo: "拼单成员的微信用户信息",
            payAccountInfo: "账单信息",
            agreeAndInitiatePayment: "同意并发起群收款",
            allOrder: "全部订单",
            shopOrder: "门店订单",
            payOrder: "买单订单",
            memberOrder: "储值订单",
            couponOrder: "券包订单",
            spellCouponOrder: "拼券订单",
            mallOrder: "商城订单",
            rightsCardOrder: "权益卡订单",
            integralMallOrder: "积分商城订单",
            pinOrder: "拼单订单",
            daojiaOrder: "外卖订单",
            goOrder: "去点单",
            goExchange: "去兑换",
            goShopping: "去选购",
            otherOnePay: "找人付",
            scanCodePay: "扫桌码下单",
            evaluateNow: "立即评价",
            survey: "填写问卷",
            viewEvaluate: "查看评价",
            confirmReceiving: "确认收货",
            confirmMeal: "完成订单",
            applyInvoice: "申请开票",
            viewInvoice: "查看发票",
            invoiceCenter: "发票中心",
            shareAccount: "分享账单",
            applyRefund: "申请退款",
            refundRecord: "退款记录",
            cancelOrder: "取消订单",
            deleteOrder: "删除订单",
            viewLogistics: "查看物流",
            wechatGroupCollection: "微信群收款",
            orderAgain: "再来一单",
            addMeal: "加菜",
            mealInfo: "用餐信息",
            mealTime: "就餐时间",
            takeorderNum: "取单号",
            yourFriendWhoHasPaidForU: "您的好友{who}已帮您付款",
            waitOrderOwnerSubmitTip: "已完成选购，等待发起人提交订单",
            youNeedPay: "您需支付",
            yourPayInfoHasUseWechatGroup: "您的账单信息将同步至微信用于群收款",
            orderHasPay: "订单支付中",
            tableNum: "桌号",
            cancelAddFood: "取消加菜",
            retry: "重试",
            orderPayErrorAndReturnedTip: "订单支付异常，已原路退回支付账户",
            remainPayTime: "剩余支付时间",
            makinggAndTakeTip: "努力制作中，请至自提门店出示取单码取餐",
            finishAndTakeTip: "餐品已制作完成，请至自提门店出示取单码取餐",
            makinggAndTakeTipOrfinishAndTakeTip: "努力制作中，请至自提门店出示取单码取餐 | 餐品已制作完成，请至自提门店出示取单码取餐",
            contactAndScanCodeTip: "请联系服务员，扫码二维码支付订单",
            writeOffInShop: "请至门店核验后商家为您制作",
            payFirstToEatTip: "请先支付才可以用餐哦～",
            addFood: "加菜",
            plaseTakeTip: "，请留意取餐提醒",
            dinnerCountdown: "出餐倒计时",
            orderMake: "订单制作",
            timeOut: "已超时",
            contactShopServerTip: "，建议联系门店人员",
            orderWillFinishTip: "订单将在倒计时内制作完成",
            contactSeller: "联系商家",
            contactRider: "联系骑手",
            contactServer: "联系客服",
            placeOrder: "去下单",
            isOnlyShowBrandPhone: "联系官方客服 | 联系店员或致电门店",
            satisfiedTip: "对门店的服务感到满意吗？",
            goFeedback: "去反馈",
            appointmentDeliveryTime: "预约送达时间为",
            appointmentTakeTime: "预约取餐时间为",
            appointmentEat: "预约就餐",
            deliverySoon: "尽快送达",
            intergral: "积分",
            fullSend: "满赠",
            newGuestsEnjoy: "新客专享",
            eatNow: "立即就餐",
            eatPeopleNum: "用餐人数",
            childNum: "儿童人数",
            expectTimeOrDelivery: "期望时间 | 预计送达",
            deliveryAddr: "配送地址",
            deliveryInfo: "配送信息",
            orderNo: "订单编号",
            accountNo: "账单号",
            placeOrderTime: "下单时间",
            payWay: "支付方式",
            payAmount: "支付金额",
            dishes: "餐具份数",
            remarksInfo: "备注信息",
            orderInfo: "订单信息",
            expectDelivery: "预计送达",
            refresh: "刷新",
            continueAddFood: "继续加菜",
            riderDelivering: "骑手正在送货",
            distanceFromU: "距离您",
            riderPicking: "骑手正在取餐",
            distanceFromShop: "距离商家",
            riderArrived: "骑手已到店",
            seller: "商家",
            consignee: "收货人",
            rider: "骑手",
            tip: "提示",
            confirmCancelOrder: "是否确认取消订单",
            thinkAgain: "再想想",
            confirm: "确定",
            cancelSuccess: "取消成功",
            confirmDeleteOrder: "确认删除订单？",
            deleteSuccess: "删除成功",
            collapseOrView: "收起全部 | 查看全部",
            "total:": "合计：",
            hasDiscounted: "已优惠",
            viewDetail: "查看详情",
            packingFee: "包装费",
            deliveryFee: "配送费",
            waitTake: "待接单",
            waitDeliver: "待配送",
            delivering: "配送中",
            hasDelivered: "已送达",
            hasPlaceOrder: "已下单",
            making: "制作中",
            pleaseTakeFood: "请取餐",
            waitingForYouFood: "待送餐",
            preparingForFood: "备餐中",
            takeMealRemindWithTable: "本店会为您送餐，入座后请耐心等待",
            takeMealRemindWithoutTable: "本店为自取餐厅，请您留意叫号屏",
            invoiceRemind: "订单完成后可开票",
            refunding: "退款中",
            refundSuccess: "退款成功",
            refundClose: "退款关闭",
            none: "无",
            ifRefundTip: "如有疑问，请",
            myOrder: "我的订单",
            orderDetail: "订单详情",
            wait: "等",
            exchange: "兑换",
            expName: "经验值",
            integral: "积分",
            pointName: "集点",
            finishOrderTSendTip: "订单完成后{t}小时内发放",
            slideSeeMore: "上滑查看更多",
            endOnlyShowOneYearTip: "到底了，仅展示近一年订单",
            callRider: "致电骑手",
            total: "共",
            itemGoods: "件商品",
            itemsGoods: "件商品",
            item: "件",
            items: "件",
            itemsOrItem: "件 | 件",
            view: "查看",
            refundContactTip: "如需退款请联系商家客服，可以提高退款效率！",
            warmTips: "温馨提示",
            giftCard: "礼品卡",
            groupMeal: "团餐",
            isSeparateDelivery: "本单商品已分开配送",
            isLoadingTips: "加载中",
            goods: "商品",
            hasNoPayResultTip: "未查询到支付结果，如您已扣款请手动查询！",
            queryPayResult: "查询支付结果",
            evaluateGain: "评价得",
            anonymousEvaluation: "匿名评价",
            uploadPic: "上传图片",
            distributionEvaluation: "配送评价",
            superpraise: "超赞",
            common: "一般",
            veryBad: "非常差",
            iRecommend: "我要推荐",
            viewAll: "查看全部",
            submitEvaluation: "提交评价",
            allGoodsInOrder: "订单中全部商品",
            storeOrderEvaluation: "门店订单评价",
            pointsMallEvaluation: "积分商城评价",
            storeName: "门店名称",
            comprehensiveScore: "综合评分",
            orderScore: "订单评分",
            merchant: "商家",
            myAdditionalComment: "我的追评",
            additionalComment: "追评",
            deleteComment: "删除",
            viewOrder: "查看订单",
            noMore: "没有更多了",
            noEvaluation: "暂无评价",
            pleasePublishYourComments: "请发表您的评价",
            hasResolved: "已解决",
            unResolved: "未解决",
            publishComment: "发表评价",
            pleaseFillCommentContent: "请填写评价内容",
            pleaseChooseHasResolved: "请选择是否已解决",
            appendCommentSuccess: "追评成功",
            confirmDeleteThisComment: "确定删除这条评价？",
            unFlagTip: "还有评价项目未评价，请先评价",
            pleaseInputComment: "请输入评价内容",
            commentSuccess: "评价成功",
            orderHasEvaluate: "订单已评价",
            thanksEvaluateTip: "感谢您的评价，欢迎下次光临",
            myRecommend: "我的推荐",
            isMallServicePaused: "已暂停商城服务",
            expected: "预计",
            pleasePatientlyWait: "，请耐心等待",
            reservePhone: "预留电话",
            payErrorTip: "支付可能遇到一些问题，请重新下单或联系客服人员",
            magicCouponPrice: "神券价"
          },
          takefood: {
            recommendPaidCardTitle: "超多权益 赶快来买",
            tablewareNum: "餐具数量",
            about: "大约",
            activityAndCouponConflictTip: "您选择的优惠与其他活动或券互斥是否确定选择？",
            actualConsumptionNHasGiftTip: "实际消费满{n}元(包含)，完成取餐后可获赠礼品",
            addFoodThisTime: "本次加菜",
            addMainGoodsFirst: "请先加购主商品",
            addOrPlus: "加 | +",
            address: "地址",
            addToCart: "加入购物车",
            addToCartBag: "加入购物袋",
            addToCartNow: "立即加入",
            afterPayNextDayReduceTip: "支付完成后，次日任意消费可",
            all: "全部",
            allGoodsInOrder: "订单中全部商品",
            alreadyIncluded: "已包含",
            amountTo: "合计",
            anonymous: "匿名",
            anonymousUser: "匿名用户",
            anotherDeliveryFee: "含配送费",
            antForestEnergyStrategy: "蚂蚁森林能量攻略",
            antForestEnergyStrategyTip: "您可以在蚂蚁森林首页查看蚂蚁森林能量具体攻略内容",
            appointmentTime: "预约时间",
            askWhetherAddToCart: "系统识别出您已预点{count}件商品，是否加入购物车？",
            aSpellFriend: "一位拼友",
            attachOutOfLimit: "该商品加料已超限制",
            attachWayIsNotSuitableTip: "该商品与{who}搭配比较奇怪，请选择小料分装",
            availableCashPoint: "可用{pointCashPoints}{pointName}抵扣{pointCashDiscount}元",
            availableCoupon: "可用优惠券",
            availablePeriod: "可用时段",
            backToHome: "返回首页",
            badEvaluation: "差评",
            bestEvaluation: "精选",
            betterSoonDeliver: "尽快送达",
            bill: "单",
            buy: "购买",
            buyCouponEnjoyDiscount: "购券包享优惠",
            buyCouponEnjoyDiscountTip: "购买特惠券包，优惠多多",
            buyRightNow: "立即购买",
            buyTogether: "一起买",
            cancel: "取消",
            cancelCustomizeSuccessTip: "取消定制成功",
            cancelFavorSuccess: "取消收藏成功",
            cancelOrderTipIfHasEquity: "您当前有{n}笔待支付订单使用了优惠券、礼品卡、余额等资产，取消订单后可返还至您的账户继续使用，现在去取消吗？",
            cancelOrExit: "取消 | 退出",
            cancelSpellTip: "取消后不会保留此次拼单内容",
            canEnjoyDiscount: "，即可享受加购特惠",
            cannotBuyTheGoodsBelow: "以下商品无法购买",
            cannotBuyTips: "抱歉，当前门店无法下单",
            cannotDeletePreGoods: "预制商品不可删除",
            cannotDeliveryTip: "特殊时期请选择无接触配送，将商品挂在家门口或放置前台，封闭管理时请电话联系",
            cannotReduce: "不能再少啦",
            canUse: "可用",
            changeShop: "更换门店",
            changeSpec: "换规格",
            choiceNofM: "{n}选{m}",
            classicMenu: "经典菜单",
            clear: "清空",
            clearCartTip: "确定清空购物袋么",
            clickAndView: "点击查看",
            clickNoTouchDelivery: "点击选择无接触配送",
            collapseOrExpand: "收起 | 展开",
            collapseOrMore: "收起 | 更多",
            colon: "：",
            comeOnAndReducePlastic: "一起来减塑",
            company: "公司",
            confirm: "确认",
            confirmAdd: "确认加购",
            confirmAfterCannotChangePayWayTip: "确认后无法更改支付方式，请联系服务员完成后续支付",
            confirmDeleteTip: "确定要删除么",
            confirmOrder: "确认订单",
            confirmUseWaiterCheckOutModeTip: "确认使用服务员结账模式么",
            congratulations: "恭喜您",
            consumptionHasGift: "消费有礼",
            contactSeller: "联系商家",
            continueOrder: "继续下单",
            continueSettlement: "继续结算",
            continueSpellOrder: "继续拼单",
            continueTakeOrder: "继续点单",
            coupon: "优惠券",
            couponDiscount: "优惠券优惠",
            couponHasLimitedTip: "优惠券数量有限，赠完即止",
            couponPreDeliveredTip: "优惠券已预发放，本单可立即使用",
            currentBill: "当单",
            currentMiniProgramVersionTooLowTip: "当前小程序版本过低，请升级您的版本后下单",
            currentPageExpiredTip: "当前页面已失效，可能您停留时间过长，请重新提交",
            delete: "删除",
            delivery: "送达",
            deliveryFee: "配送费",
            deliveryFeeNPrice: "配送费{n}元",
            deliveryOvertimeCompensation: "外卖超时赔付",
            deliveryQuestionTip: "配送费受配送距离、难度、时段、重量、运力等因素影响,商户首页及商品浏览页展示的配送费仅为预估配送费金额,最终以订单结算页显示的配送金额为准。",
            deliveryTime: "送达时间",
            deliveryTip: "由{who}提供配送服务（配送范围受地区、天气等多方因素影响，以实际可配送距离为准）",
            detail: "详情",
            determine: "确定",
            dinersNum: "用餐人数",
            distanceYou: "距您",
            distribute: "配送",
            distributeFromWho: "由{who}配送",
            distributeTo: "配送至",
            dividePackage: "分装",
            dividePackageAndIndependent: "分装（独立分包）",
            douyin: "抖音",
            eatIn: "堂食",
            eatInOvertimeCompensation: "堂食超时赔付",
            elderMode: "长辈模式",
            encryptionProtection: "加密保护",
            estimated: "预估",
            evaluation: "评价",
            exchangeNow: "立即兑换",
            exit: "退出",
            exitSpellTip: "退出后不会保留此次拼单内容",
            expand: "展开",
            expectDeliveryTime: "期望送达时间",
            expectedSaveNprice: "预计省￥{n}",
            expectedSaving: "预计节省",
            expectedToGetInThisOrder: "本单预计可获得",
            expireAfter: "后失效",
            favorShopSuccess: "收藏门店成功",
            favorTasteSuccessTip: "收藏口味成功",
            finish: "完成",
            foodsWillBeReadyBefore: "，餐品将在预约时间前",
            friendsOrder: "好友点单",
            friendSpell: "好友拼单",
            from: "起",
            fullGift: "满赠",
            fullGiftSupportWords1: "恭喜您获得赠品，请选择，最多{n}件",
            fullGiftSupportWords2: "恭喜您获得{n}件赠品",
            fullGiftMaxLimit: "该笔订单最多选择{n}件",
            fullGiftMoreLimit: "最多选择{n}件",
            plaseSelectGift: "请选择赠品",
            happilyAccept: "开心收下",
            abandonGift: "放弃赠品",
            totalGifts: "共赠送{n}件赠品",
            mostGifts: "最多{n}件",
            abandonGiftsTips: "确定放弃所有已选择的赠品？",
            getGift: "我要赠品",
            alreadyAbandonGifts: "赠品已放弃",
            give: "赠送",
            fullGiftOrChange: "满赠 | 超值换购",
            full: "满",
            pieceToUse: "件可用",
            priceToUse: "元可用",
            fullN: "满{n}",
            fullNPieceToUse: "满{n}件可用",
            fullNPriceToUse: "满{n}元可用",
            fullPlus: "特惠加购",
            fullReduceDiscount: "满减优惠",
            gatherOrderNow: "立即凑单",
            getPhone: "获取号码",
            giftCard: "礼品卡",
            giftCoupon: "好礼券",
            giftMaxSelectedTip: "赠品最多可选{n}件",
            goCustomize: "去定制",
            goModify: "去修改",
            goodEvaluation: "好评",
            goodsCoupon: "商品券",
            goOrder: "去下单",
            goSelectPartner: "去选伴侣",
            goToAdd: "去添加",
            goToAuth: "去授权",
            goToBuy: "前往购买",
            greenAndCheapTip: "助力环保，立享优惠",
            growthValue: "成长值",
            hasChoose: "已选",
            hasMainFoodWarmTips: "温馨提示: 您点主食了吗?",
            hasRecommendDiscount: "已为您推荐更优折扣方案",
            hasSoldout: "已售罄",
            haveChosen: "选好了",
            haveImage: "有图",
            home: "家",
            hour: "小时",
            iknow: "我知道了",
            independentPackage: "独立分包",
            initiator: "发起人",
            inProductionAndWait: "制作中，预计等待",
            inPurchase: "选购中",
            inputContactPhone: "请填写联系人手机号码",
            inputFavorRequire: "请输入口味、偏好等要求",
            inputReservedPhone: "选填，便于订单异常时联系",
            instructions: "使用说明",
            integralDeduction: "积分抵扣",
            invalidGoods: "失效商品",
            inviteFriends: "邀请好友",
            inviteSpellOrder: "邀您一起拼单啦",
            isNotifyKitchen: "是否通知后厨为您先预制{name}",
            last: "剩余",
            limitBuyPerOrder: "每单限购{n}份哦",
            limitDiscountNZhe: "限时折扣{n}折",
            limit: "限",
            limitNPiece: "限{n}件",
            limitReduceNYuan: "限时立减{n}元",
            limitSaleNYuan: "限时特价{n}元",
            limitUseOneCouponPerGoods: "（每件商品限用1张）",
            limitUseOneCouponPerOrder: "（每单限用1张）",
            login: "登录",
            lowAs: "低至",
            make: "制作",
            maxNAttachTip: "最多选购{n}份加料哦！",
            maxNPieceMTip: "最多选购{n}份{m}哦！",
            maxReduce: "最高可减",
            maxSelectedInGroup: "分组下至多选择{n}件！",
            maxSelectedTip: "最多可选{n}件",
            me: "我",
            measurementUnit: "计量单位",
            meituan: "美团",
            memberBalance: "会员余额",
            memberCardDiscount: "会员卡优惠",
            memberPrice: "会员价",
            middleEvaluation: "中评",
            miniappCodeErrorTip: "小程序码有误，请重新扫描",
            minLimitNAttach: "需要选购{n}份加料哦！",
            minPieceToBuy: "件起购",
            minutes: "分钟",
            monthSale: "月售",
            moreFavorable: "更优惠",
            mutexWithOtherTip: "与{what}互斥，是否确定选择？",
            mutexWithWhoSelectedTip: "【{who}】与已选项不能同时选中",
            myOrder: "我的点单",
            myTaste: "我的口味",
            nCoupon: "{n}张{couponName}",
            nCouponExchangeTip: "您的兑换券还可以选择{n}件商品",
            needAuthTip1: "为了给你提供更好的拼单服务体验",
            needAuthTip2: "请先授权微信个人信息",
            needDinnerwareDueToTip: "需要餐具，依据餐量提供",
            needLoginAndEnjoyTip: "以下活动需登录后参与，否则无法给你发放优惠券、积分等权益",
            needSelectGoods: "您还需要选择以下商品后才可下单",
            networkErrorContactServiceTip: "当前门店网络异常，请联系店内工作人员为您服务",
            newCustomerEnjoy: "新客专享",
            nextDayCanReduce: "明日可减",
            nextDayReduce: "次日减",
            nManHasOrder: "{n}人已点完",
            nManOrdering: "{n}人正在选购",
            noAdd: "不加购",
            noAnyEvaluationFTM: "暂时还没有任何评价",
            noCodeInfoTip: "未识别到码信息",
            noCouponAreAvailable: "暂无可用优惠券",
            noDividePackage: "不分装",
            noEnableCouponsForNow: "暂无可用券",
            noFriendsJoinSpellTip: "暂无好友加入拼单，快去邀请吧",
            noGoodsInPocket: "该口袋暂未加购商品",
            noNeed: "不用了",
            noNeedDinnerware: "无需餐具",
            noNeedQueue: "免排队",
            noNeedQueueCoupon: "免排队券",
            noNeedToWaitTip: "您当前下单购买的商品无需等待，可直接向店员取餐",
            nOrderProcessing: "{n}笔{type}订单，共计{m}{unit}商品制作中",
            normalMode: "普通模式",
            noSelectedGoods: "暂无商品，请先选购",
            noSelectGoodsTip: "您还没有选择商品",
            noSelectedFood: "未选购商品",
            notBusinessTime: "未到营业时间",
            notCountInPiece: "，小料不计入商品件数",
            notDeliveryIfOnlyOne: "单点不配送",
            notEnough: "不足",
            noThreshold: "",
            notifyKitchenContactServiceTip: "预制后不可调换，如需调换请联系服务员",
            notReturnGoodsPointTip: "部分商品发起退款时{pointName}将不会退还",
            saleDate: "售卖日期",
            sellingTime: "售卖时间",
            notSaleTime: "非售卖时间",
            notSendIfOnlyOne: "单点不送",
            notShareWithOther: "该优惠不与其他优惠共享",
            notSupportSpellTip: "抱歉，该门店暂不支持拼单，换个门店再试试！",
            notSupportTakeout: "不支持外卖点单",
            notSupportTakeoutTip: "当前门店暂不支持外卖点单，您可以选择其他门店",
            notUseForNow: "暂不使用",
            noWhatCouponAreAvailable: "暂无可用{what}券",
            nPart: "{n}份",
            nPieceAreAvailable: "{n}张可用",
            nPieceStartDistribute: "{n}件起送",
            nPriceStart: "{n}元起",
            nPriceStartDistribute: "{n}元起送",
            nTicketsAvailable: "{n}张可用",
            nTicketsLeft: "剩{n}张",
            numberOfDiners: "就餐人数",
            nYuanNextDayReduceNotUsed: "{n}元次日减优惠未使用，",
            ok: "好的",
            onCupMaxNAttachTip: "单杯不可大于{n}份加料",
            onCupMaxNAttachWhatTip: "单杯不可大于{n}份{what}",
            oneCouponPerOrder: "每单限用一张",
            oneKeyAA: "一键AA",
            oneSpellFriend: "一位拼友",
            onlyOneAttach: "该分组仅可选择一种加料",
            openAndEnjoyDiscount: "开通享折扣",
            openNow: "立即开通",
            optional: "可选",
            orderAndHasChanceToLottery: "下单即有机会参与抽奖",
            orderedFood: "已下单菜品",
            orderHistory: "历史点单",
            orderSubmitting: "订单提交中",
            orderTooManyNotice: "当前门店订单过多，暂不可接单，可以接单时，将通过订阅消息提醒您",
            otherPay: "找人付",
            outOfDeliveryRange: "超出配送范围",
            packageFee: "包装费",
            packingFee: "打包费",
            part: "份",
            payFullHowMuchAndReduceHowMuch: "实付满{fullHowMuch}，最高可减{reduceHowMuch}元",
            payOrOder: "提交支付 | 确认下单",
            payWay: "支付方式",
            peaceMindTips: "安心小贴士",
            people: "人",
            phoneError: "手机号有误",
            phoneProtected: "号码保护",
            phoneProtectedToRiderTip: "对骑手隐藏您的真实手机号，保护您的隐私为保障服务质量， 开启号码保护的订单通话可能会被录音",
            piece: "件",
            pinTogether: "一起拼",
            pleaseLoginAndEnjoy: "请登录后参与活动",
            pleaseScanTableCodeFrist: "请先扫桌码",
            pleaseSelect: "请选择",
            pleaseSelectDeliveryAddr: "请选择收货地址",
            pleaseSelectDinersNum: "请选择就餐人数",
            pleaseSelectGoods: "请选择商品",
            pleaseSelectGoodsFrist: "请先选择商品",
            pocket: "口袋",
            preferentialActivities: "优惠活动",
            priceOrPiece: "元 | 件",
            putIn: "装入",
            putInPocketTip: "选用后，加购商品将自动放入该口袋",
            queryAfterLogin: "登录后查询",
            queryWhetherAddToCart: "系统识别出您已预点 {n} 件商品，是否加入购物车？",
            quickInput: "快捷输入",
            randomReduce: "随机立减",
            reachExchangeLimit: "已达到兑换上限",
            rechargeAgree: "储值即同意",
            rechargeAmountArrived: "储值金额已到账",
            storedValueReminder: "储值金额已到账 | 储值金额、赠券已到账",
            recommand: "推荐",
            recommendCollocation: "超值加购",
            recommendFood: "推荐菜",
            recommendSelect: "推荐选择",
            recommendTasteTip: "为您推荐适合此款商品的口味搭配～",
            recommendTasteTip2: "选择喜欢的口味，助您下次快捷点单～",
            recommendTasteTip3: "已为您推荐喜欢的口味搭配，助您快捷点单～",
            recommendTasteTip4: "更新喜欢的口味搭配，下次可以快捷点单~",
            redBagDiscount: "红包优惠",
            reduceNDeliveryFee: "减{n}元配送费",
            reduceNPrice: "立减{n}元",
            remark: "备注",
            remarkMainGoods: "备注主商品",
            required: "必选",
            requiredGoodsNotReduce: "必选商品不可减少哦",
            reselectShop: "重新选择门店",
            reservedPhone: "预留电话",
            restoreDefault: "恢复默认",
            rmb: "rmb",
            sameGoodsCannotSpell: "相同商品不可多拼",
            saveDeliveryFee: "免配送费",
            saveZeroDiscount: "抹零优惠",
            scanCodeExpired: "上次扫码已经过期啦，请重新扫码",
            scanTableCode: "扫桌码",
            school: "学校",
            searchGoods: "搜索商品",
            securityTipsText: "疫情期间，本店严格遵守防疫政策，保障您和家人的安全",
            selectDistributeAddr: "请选择配送地址",
            selected: "已加购",
            goToUse: "去使用",
            goToExchange: "去兑换",
            selectedGoods: "已选商品",
            selectGoods: "选择商品",
            selectOne: "任选一款",
            selectShop: "选择门店",
            selectSpec: "选规格",
            selectCombo: "选套餐",
            selectSpecOrCombo: "选规格 | 选套餐",
            selectValidSpecTip: "请选择有效规格",
            selectWhatGoods: "选择{what}商品",
            goods: "商品",
            selfCup: "自带杯",
            selfCupNotShareTip: "自带杯商品不与券或活动同享",
            selfCupOnlineTip: "自带杯功能上线啦！",
            sellerGift: "商家赠送",
            sellerPhone: "店长电话",
            sellerRecommend: "商家推荐",
            sellerReply: "商家回复",
            sendNCoupns: "送{n}张券",
            send: "送",
            pieceCoupon: "张券",
            sendTo: "送到",
            setPassword: "设置密码",
            shopBusinessTime: "门店营业时间",
            shopDetailInfo: "门店详细信息",
            shopFixedLine: "门店固话",
            shopInfo: "门店信息",
            shopNotice: "门店公告",
            shopPhone: "门店电话",
            shortNPieceStartDistribute: "差{n}件起送",
            shortNPriceStartDistribute: "差{n}元起送",
            shortOfBalance: "余额不足",
            soldoutTip: "抱歉，已售罄",
            soldOutToday: "今日售罄",
            spellHasCancelTip: "发起人取消了拼单",
            spellHasCommitTip: "拼单已提交",
            spellOrder: "拼单",
            spellOrderLockedTip: "拼单已锁定，无法修改商品",
            spellOrderProcessing: "拼单进行中",
            spellOrderText: "好友来拼单，分账无需算",
            startDistribute: "起送",
            stillShort: "还差",
            stockNotEnough: "库存不足",
            storedOrAmount: "储值 | 合计",
            storeOpenNotice: "门店开始营业时，我们将以服务通知的方式通知您",
            stow: "收起",
            superValueAddGoods: "起超值加购以下商品",
            tableHasOccupiedTip: "桌位被占用，请联系商家",
            tableIsLockedContactServiceTip: "当前桌台被锁定，请联系店内工作人员为您服务",
            tableNo: "桌号",
            takeMeal: "取餐",
            takeout: "外卖",
            TAsRecommend: "TA的推荐",
            tasteAndFavorRequire: "口味、偏好等要求",
            tasteCard: "风味卡",
            thereMoreAhead: "前面还有",
            thisOrderHasCouponNotUsedTip: "本笔订单有可使用优惠券未使用哦，是否立即使用？",
            time: "时间",
            tips: "提示",
            toady: "今天",
            tooFarFromShopTip: "您距离该门店太远了，请靠近一点再下单",
            toPrepare: "准备吧",
            toSettle: "去结算",
            total: "共",
            totalDiscount: "共优惠",
            totalOfN: "共{n}",
            itemsOrItem: "件",
            totalNPiece: "共{n}件",
            totalSale: "总售",
            totalSelected: "全选",
            ttCouponVerificationFail: "抖音券核销失败",
            unauthorizedPositioning: "未授权定位",
            understood: "已了解",
            unlockAfterUpgrade: "升级后解锁",
            unsalableGoods: "不可售商品",
            unselected: "未选择",
            useCouponToPayHasGiftTip: "使用当前优惠券支付，完成取餐后可获赠礼品",
            useImmediately: "立即使用",
            useOfThreshold: "使用门槛",
            userNickname: "用户昵称",
            useThisCoupon: "使用该优惠券",
            useEntityCard: "使用实体卡支付",
            useRightsCard: "选择付费会员搭售",
            validPeriod: "有效期",
            view: "查看",
            info: "查看",
            viewAvailableTime: "查看可售时间",
            viewSaleTime: "查看开售时间",
            availableTime: "可售时间",
            saleTime: "开售时间",
            remindMe: "提醒我",
            viewDetail: "查看详情",
            viewFoodSafetyFiles: "查看食品安全档案",
            viewOrder: "查看订单",
            viewShopServiceQualification: "查看门店服务资质",
            waiterCheckOut: "服务员结账",
            waiterCheckOutTip: "（如需使用纸质优惠券或现金等）",
            warmTips: "温馨提示",
            confirmUse: "确认使用",
            thinkAgain: "再想想",
            weekIs: "周日 | 周一 | 周二 | 周三 | 周四 | 周五 | 周六",
            weekSale: "周售",
            whatCannotSupportWhichActivityTip: "{what}不支持已参与的{which}活动，切换享用方式后将清除已选的活动商品，是否确认切换？",
            whatCanSelectNPiece: "{what}只能选择{n}件",
            whatCanSelectNPiecePerOrder: "{what}每单只能选择{n}件",
            whatGoodsMaxNPiece: "{what}中商品最多购买{n}件哦",
            whatRequiredTip: "{what}必选哦！",
            whichGoodsNeedAttach: "您需要把加料加在哪个商品上呢？",
            wishesWords: "寄语",
            writeToYourselfOrTa: "写给自己，或给Ta",
            yibai: "易百",
            youHaveMakeAppointment: "您预约了",
            youHaveUsedNoQueueCoupon: "您已使用免排队券，门店会优先给您制作。",
            zhifubao: "支付宝",
            paying: "支付中",
            paySuccess: "支付成功",
            viewOrderDetail: "查看订单详情",
            continueBuy: "继续购买",
            balance: "余额",
            cannotUseBalanceTip: "与已参与优惠无法同享 | 与订单已参与优惠不可同享，如需使用余额支付，请重新下单！",
            hasFrozen: "已冻结",
            orderFullNYuan: "订单实付满{n}元，",
            fullOrder: "整单",
            useBalancePayCanSaveNYuan: "使用储值余额支付，立省{n}元",
            subscribeBalanceChangeReminder: "订阅储值余额变动提醒",
            useThisBalancePayCanSaveNYuan: "选择当前储值并支付，立省{n}元",
            shortOfBalanceChangeTip: "余额不够支付，不支持混合支付，请充值",
            wechatPay: "微信支付",
            alipayPay: "支付宝支付",
            officalPay: "官方支付",
            payNow: "立即支付",
            frozenDesc: "冻结说明",
            goodsSoldOutCheakNearbyShop: "商品已售罄，查看附近门店",
            specNotAddSelectOther: "该规格不可加购，请选择其他规格",
            exchangeNPiecesAtOneTime: "一次最多只能兑换{n}件",
            energy: "能量",
            lastMaxCanExchangeN: "剩余最多可兑换{n}件",
            today: "今天",
            select: "选择",
            exclusiveOffer: "专享优惠",
            confirmPay: "确认支付",
            storeValue: "储值",
            nOrder: "{n}笔{type}订单，",
            nGoodsProcessing: "共计{n}{unit}商品制作中",
            nearByShop: "附近门店",
            more: "更多",
            choice: "选",
            remain: "剩",
            sheet: "张",
            recommandShopTip: "已为您推荐最近门店",
            recommandAddrTip: "已为您推荐收货地址",
            shop: "门店：",
            deliverShop: "配送门店：",
            mealWay: "用餐方式",
            mealTime: "用餐时间",
            mealNum: "用餐人数",
            confirmPayWay: "确认支付方式",
            weixinPay: "微信支付",
            zhaohangyiwangtongPay: "招行一网通支付",
            selectBlindBox: "选盲盒",
            selectCoupon: "选择优惠券",
            notSelectCoupon: "不使用券",
            useSystemRecommend: "使用系统推荐最优方案",
            hasChooseNCouponsTotaloffset: "已选{n}张，可抵用",
            pleaseSelectCoupon: "请选择优惠券",
            useRecommend: "帮我推荐最优折扣",
            unavailableCoupon: "不可用券",
            noCouponsAvailable: "暂无可用的优惠券",
            merchantCoupon: "商家券",
            activityCoupon: "活动券",
            recommandUseDiscountTip: "推荐使用活动折扣更优",
            specificGoodsTip: "该优惠券需特定商品使用，不使用{x}，将删除{y}！",
            notUseThisCoupon: "不用该券",
            thinkAboutIt: "考虑一下",
            isBetterDisounctTip: "当前选择已是更优折扣",
            specialTimeTip1: "请输入口味、偏好等要求",
            inputTasteTip: "请输入口味、偏好等要求",
            activityDiscount: "活动优惠",
            exchangeEquity: "兑换权益",
            equityOrGift: "权益 | 礼品",
            orderEquity: "本单权益",
            orderEquityTip: "此处为预估积分、成长值的数量，您的支付方式以及会员等级权益等均可能影响积分、经验的计算，以最终下单后到账情况为准。",
            servivePhone: "客服电话",
            times: "次",
            tempSoldOutTip: "本店暂时售罄",
            storeValueEnjoy: "储值享",
            friendlyTips: "温馨提示：请适量点餐、避免浪费",
            eatNow: "立即就餐",
            takeMealNow: "立即取餐",
            sendRightNow: "尽快送达",
            plaseSelectAppointmentTime: "请选择预约时间",
            selectAppointmentTime: "选择预约时间",
            selectArrivalTime: "选择送达时间",
            appointmentEat: "预约就餐",
            appointmentTakeTime: "预约取餐",
            deliverToHome: "配送到家",
            takeByMySelf: "到店自取",
            physicalCardPay: "实体卡支付",
            giftCouponHasArrived: "赠券已到账",
            selectMeal: "已选餐品",
            plus: "加",
            hasBuy: "已买",
            selectOneGoodsTip: "请至少选择1件可优惠子商品",
            canDiscount: "可优惠",
            none: "空",
            whatLimitN: "【{what}】限{n}件",
            limitBuy: "限购",
            startBuy: "起购",
            attachGroup: "加料分组",
            attachGroupMinN: "加料分组必选{n}份",
            limitBuyNPart: "限购{n}份",
            replace: "替换",
            noReplace: "不替换",
            replaceTip: "是否替换购物车中的",
            onlyCanUseOneCouponTip: "此优惠券每单限用一张",
            hasReplaceGoods: "已换购",
            goReplaceGoods: "去换购",
            clickToStowOrViewDetail: "点击收起 | 查看详情",
            quan: "券",
            attachGroupNStartBuy: "加料分组{n}份起购",
            xGroupNLimitBuyNPart: "{x}分组限购{n}份",
            xGroupNStartBuy: "{x}分组{n}份起购",
            xGroupNRequired: "{x}分组必选{n}份",
            conflictWithSelectedTip: "与已选选项冲突",
            WhatNoMoreLastNTip: "{what}库存不足，剩余{n}件~",
            chooseNWhat: "请选择{n}款{what}商品",
            chooseLimitNWhat: "请在{what}中选择至少{n}商品",
            notSupportPayTip: "不支持混合支付，实体卡余额不足",
            noMoreBalance: "您的余额不足",
            notSupportPayTip2: "推荐券包或者推荐权益卡部分不能使用余额支付",
            WhatMaxBuyN: "{what}最多只能购买{n}个哦！",
            WhatMinBuyN: "{what}最少购买{n}个哦！",
            remainPayTime: "剩余支付时间",
            heat: "热量",
            maximumPurchaseOfGoods: "{what}商品最多购买{n}个哦",
            chooseMaxNWhat: "请在{what}中最多选择{n}件商品",
            orderNowWillWaitTime: "现在下单，预计等待",
            inProgressWillWaitTime: "制作中，预计等待",
            inProgressWill: "制作中，预计",
            goodsinProgressWill: "商品制作中，预计",
            goodsinProgressWillWait: "商品制作中，预计等待",
            goodsinProgressPleaseWait: "商品制作中，请耐心等待",
            subscribed: "已订阅",
            storeDeliveryRange: "当前门店已超出配送范围，请选择其他可配送门店",
            goodsinProgressSuccess: "商品已制作完成，请及时取餐",
            edit: "编辑",
            latestShortNotes: "最多显示最近20个快捷备注",
            alreadyHasDisounctTip: "已享受折扣优惠，共减免",
            imeChangeConfirmTips: "切换就餐方式可能会导致购物车显示优惠与实际不符，请以结算页优惠为准~",
            Notredemption: "n不足，无法参与换购",
            Onlyoneredemption: "一单只能换购一件商品",
            Exchange: "换",
            Offset: "抵扣",
            my: "我的",
            Tradein: "换购",
            BuyOneGetOneFree: "买一送一",
            receiptGoodsTips: "确认收到货了吗?",
            RecommendedExchange: "推荐换购",
            OneclickExchange: "一键换购",
            ExchangePrice: "换购价",
            ExchangeSuccessful: "换购成功",
            inventoryNotEnough: "当前商品库存不足，请重新选择",
            notUseDiyName: "不使用{what}",
            recommandUseDiyName: "推荐使用{what}，锁住新鲜口感",
            useCanHeDesc: "保冷保鲜保温，锁住新鲜口感",
            notUseCanHeDesc: "无保冷保鲜保温效果",
            canhefeiRecommend: "推荐选择",
            includeChildNum: "含{n}儿童"
          },
          user: {
            whoInviteFeedback: "{who}邀请您进行建议反馈",
            submitSuccess: "提交成功",
            doNotInputBlindly: "纯数字，纯字母不利我们快速定位问题喔",
            askWhatOrder: "请选择您要反馈的订单",
            askIsThisOrder: "Hi, 请问您要反馈的是这笔订单么?",
            addImage: "添加图片",
            suggestionPlaceholder: "5字以上清晰描述您的反馈，我们会尽快处理",
            collapseOrExpand: "收起 | 展开",
            helpForBetter: "帮助我们做的更好",
            helpForHappier: "每份建议，都会用心处理，建议采纳有机会获好礼相赠",
            memberCode: "会员码",
            adopted: "已采纳",
            hasAcceptFeedback: "商家已接收反馈",
            noFeedback: "暂无建议反馈",
            makeSuggestions: "欢迎小主提建议",
            shopReply: "商家回复",
            loginText: "为给您提供更好的服务请授权登录",
            loginText2: "新人登录享受更多优惠",
            loginAndRegister: "登录 / 注册",
            membersRights: "会员权益",
            user: "用户",
            maxLevelTip: "恭喜你，已达最高等级",
            getNWhatAndUpgradeLevel: "再获得{n}个{what}可升级为{level}",
            goPerfect: "去完善",
            viewPoint: "查看积分",
            viewCoupon: "查看优惠券",
            viewBalance: "查看余额",
            viewGiftCard: "查看礼品卡",
            viewCardbag: "查看卡包",
            viewEquityCard: "查看权益卡",
            viewEntityStoredCard: "查看实体卡",
            ge: "个",
            notUsed: "未使用",
            youHaveOneCardToGet: "您有一张会员卡待领取",
            receiveNow: "立即领取",
            modeNormalOrElder: "普通模式 | 长辈模式",
            qmaiSupport: "企迈提供技术支持",
            pleaseInputBalancePayPassword: "请输入余额支付密码",
            forgetPayPassword: "忘记支付密码",
            myFunction: "我的功能",
            myOrder: "我的订单",
            myAssets: "我的资产",
            myServer: "我的服务",
            promoters: "推广员",
            personalServer: "个人服务",
            notYet: "暂不",
            confirm: "确定",
            confirmToSwitchWhatTip: '确定将语言切换为"{what}"?',
            order: "订单",
            shopOrder: "门店订单",
            buyOrder: "买单订单",
            storedOrder: "储值订单",
            couponOrder: "券包订单",
            pinCouponOrder: "拼券订单",
            mallOrder: "商城订单",
            langConfig: "语言设置",
            sheet: "张",
            balance: "余额",
            yuan: "元",
            redPack: "红包",
            cardbag: "卡包",
            equityCard: "权益卡",
            entityStoredCard: "实体卡",
            receiveCoupon: "领取优惠券",
            goToView: "前往查看",
            goMiniApp: "去小程序逛逛",
            receiveSuccess: "领取成功",
            couponHasReceive: "优惠券已领取",
            couponHasBack: "优惠券已退回",
            couponHasCancelSend: "优惠券已取消赠送",
            couponHasTimeout: "优惠券赠送超时",
            couponHasRecovery: "优惠券已回收",
            yourFriendsReceiveCouponTip: "您的好友{who}领取了优惠券",
            nickName: "昵称",
            phoneNum: "手机号",
            gender: "性别",
            birthday: "生日",
            accountAndSecurity: "账号与安全",
            save: "保存",
            exit: "退出登录",
            changePhoneNumber: "更换手机号",
            male: "男",
            female: "女",
            fillIn: "请填写",
            pleaseAuthPhone: "请授权手机号",
            updateBirthdayTip: "商家可能会根据生日推出相关优惠活动，您可修改一次个人生日，确定修改吗？",
            reAuthPhoneTip: "重新授权将清除当前已绑定的手机号， 是否确认操作？",
            updateSuccess: "更新成功",
            updateBirthdayNotSupportTip: "涉及会员权益，不支持二次修改",
            confirmLogoutTitle: "确定退出登录？",
            logoutTip: "退出后将无法查看订单相关信息",
            confirmLogout: "确定退出",
            PersonalProfile: "个人资料",
            RequestRefund: "申请退款",
            UnableNickName: "昵称不合规，请修改",
            offlineBalancePaymentPassword: "线下余额支付密码",
            resetInSomeSeconds: "{s}秒后自动重置，仅在店内线下使用",
            offlineBalancePaymentPasswordTip: "门店人员线下收银扣减您账户余额时，可将该密码告知门店人员；该密码会自动重置，无安全隐患；"
          },
          shop: {
            selectShop: "选择门店",
            receiveAddress: "收货地址",
            nearByAvailableShop: "收货地址附近可提供配送的门店",
            callSuccess: "召唤成功",
            inBusiness: "营业中",
            eatInNotAvailable: "暂不支持堂食",
            inRest: "休息中",
            findReceiveAddress: "已找到收货地址",
            confirmUse: "确认使用",
            changeAddress: "换个地址",
            selectThis: "就选这家",
            goCharge: "去充值",
            goChange: "去兑换",
            overDelivery: "超出配送范围",
            goBuyOrder: "去买单",
            goTakeOrder: "去下单",
            goLook: "去看看",
            noPinGroupThisShop: "当前门店不可拼团",
            noBuyCouponThisShop: "当前门店不可购券",
            shopBusy: "门店繁忙",
            shopBusyTip: "目前门店单量过多，因此我们不得不暂停该门店线上点单，您可切换其他门店下单，非常抱歉，敬请谅解。",
            entryShop: "进入门店",
            farTip: "您当前所在位置距离该门店较远，是否继续点单",
            waitAMinute: "请稍后",
            groupCouponNoApplicable: "团购券不适用该门店",
            noResults: "暂无相关结果",
            changeWord: "请尝试更换门店名称或地址关键字",
            changeStoreName: "暂无相关结果，请更换门店名称关键词",
            acceptPreOrder: "接受预定",
            bill: "单",
            canBuyCouponOrSepll: "可购券 | 可拼团",
            canOrderOnline: "可在线点单",
            canTakeout: "可外卖",
            cityHas: "当前城市已有",
            favor: "收藏",
            getAddressLocation: "开启位置授权",
            iKnow: "我知道了",
            iWillCall: "我要召唤",
            iWillJoin: "我要加盟",
            locationUnauthorizedTip: "位置信息未授权，无法获取您的定位~",
            nearBy: "附近",
            noShopNearby: "附近暂无门店~",
            noShopNearbyToSelectOtherCity: "您附近暂无门店，可选择城市查看其他门店",
            notOrderOnlineBelow: "以下门店不可在线点单",
            orderNowAndMakeNow: "现在下单，立即制作",
            peopleAnswerCall: "人参与召唤",
            recommendShopWithlocation: "根据当前定位为您推荐以下门店",
            search: "搜索",
            searchShop: "搜索门店",
            selectOtherCity: "选择其他城市",
            test: "测试",
            businessCloseTodayTip: "今日暂停营业",
            openSoon: "即将开业",
            businessClose: "暂停营业",
            oftenGo: "常去",
            storeIsClosedChooseOtherStore: "门店已休息，可尝试选择其他门店",
            front: "前方",
            storeIsClosedMealCanAvailable: "门店已休息，可预约点餐",
            PleaseSelectStore: "请选择门店",
            PleaseSelectCity: "请选择城市",
            locationUnAuthTip: "请先授权当前定位，或选择城市查看门店",
            locationAuthErrorTip: "当前定位失败，请检查系统定位设置，或选择城市查看门店",
            takeoutLocationUnAuthTip: "请先授权当前定位，或选择收货地址查看门店",
            takeoutLocationAuthErrorTip: "当前定位失败，请检查系统定位设置或选择收货地址查看门店",
            selectDeliveryShop: "选择配送门店",
            selectCity: "选择城市",
            takefoodSearchNull: "暂无搜索结果，请更换门店名称或地址关键词",
            "NoStoreContactInformatioAvailable.": "暂无门店联系方式",
            MerchantProfile: "商家档案",
            switch: "切换"
          },
          marketing: {
            go: "可至",
            mine: "我的",
            view: "查看",
            pieces: "张",
            newUser: "新用户",
            coupon: "优惠券",
            unlimited: "",
            placeOrder: "去下单",
            loginAuth: "授权登录",
            activityRule: "活动规则",
            obtainedNotice: "您已获得",
            exchangeCoupon: "兑换券",
            thresholdAmount: "满{n}元可用",
            thresholdWeight: "满{n}千克可用",
            thresholdQuantity: "满{n}件可用",
            forInStoreUseOnly: "限线下使用",
            claimCouponNow: "立即领券",
            loginForCoupon: "立即登录领券",
            availableCoupon: "可领取优惠券",
            couponInAccount: "优惠券已放入您的账户",
            canAddToWeChatCardPackage: "可加入微信卡包",
            couponsAvailableUponLogin: "登录后可领取以下优惠券",
            useIt: "去使用",
            useRule: "使用规则",
            giveFriends: "送好友",
            applicableBrands: "适用品牌",
            applicableStores: "适用门店",
            applicableProducts: "适用商品",
            applicableChannels: "使用渠道",
            applicableScenarios: "使用场景",
            usePeriod: "使用时段",
            useExplanation: "使用说明",
            couponSource: "券来源",
            useThreshold: "使用门槛",
            useLimitation: "使用限制",
            validityPeriod: "有效期",
            discountCap: "优惠上限",
            discountMethods: "优惠方式",
            couponID: "优惠券ID",
            payMethodLimit: "限制支付方式",
            couponList: "优惠券列表",
            defaultsorting: "默认排序",
            latestacquisition: "最新获得",
            almostdue: "即将到期",
            allcoupons: "全部优惠券",
            invalid: "已失效",
            ineffective: "未生效",
            allscenes: "全部场景",
            dinein: "堂食",
            outband: "外带",
            takeout: "外卖",
            payment: "买单",
            mall: "商城",
            historicalcoupons: "历史优惠券",
            pointsmall: "積分商城",
            pointsdetails: "积分明细",
            integralrule: "积分规则",
            effective: "已生效",
            details: "明细",
            rule: "规则",
            viewMd: "查看门店",
            viewGoods: "查看商品",
            all: "全部门店",
            available: "指定门店适用",
            unavailable: "指定门店不适用",
            allGoods: "全部商品",
            availableGoods: "指定商品适用",
            unavailableGoods: "指定商品不适用",
            paymentMethodRestrictions: "是否整单使用指定支付方式支付",
            storedValueBalance: "储值余额",
            noLimit: "不限",
            payAllAmount: "整单金额支付",
            payAnyAmount: "任意金额支付",
            unlimitedCoupon: "",
            canUse: "可用",
            free: "免",
            discount: "折",
            reducedTo: "减至",
            validUntil: "有效期至",
            daysRemainingUntilExpiration: "距过期仅剩{n}天",
            hoursAndMinRemainingUntil: "距过期仅剩{m}时{n}分",
            used: "已使用",
            noUsedWhitOther: "本优惠券不可与其他营销活动共享",
            reasonForUn: "不可用原因",
            noMinimumOrderAmount: "无订单金额限制",
            expired: "到期",
            freeShipping: "免运费",
            freePrice: "免费",
            AddOneClick: "一键加购",
            nextDayDiscount: "次日减",
            nextDayNOff: "明日可减",
            selectGuiGe: "请选择规格",
            addGift: "一键添加赠品",
            addUptoN: "每单最多加购{n}件",
            addgoods: "请选择加购商品",
            exchangeGoods: "兑换商品",
            clickToClaimNowToAddWechatWallet: "点击“立即领取”可加入微信卡包",
            receiveSuccess: "领取成功",
            addedToCardWalletSuccessfully: "加入卡包成功",
            addedToCardWalletFailed: "加入卡包失败",
            couponButtonClicked: "点击下方按钮领取优惠券",
            startTime: "开始时间",
            endTime: "结束时间",
            haveBeenCollectedNCoupons: "您已领取 {n} 张优惠券",
            haveCollected: "已集齐{n}",
            canReceiveNCoupons: "可领取{n}张优惠券",
            currentStarQuantity: "当前{star}数量",
            also: "还有",
            pending: "待生效",
            needToUseCouponToContinueStar: "使用完上次获得的优惠券才可继续获得{star}",
            couponRedeemedCheckAssetsPage: "已兑换成优惠券，请前往资产页面查看",
            isUserNotAuthorized: "您当前还未授权登录哦~",
            isActivityNotStarted: "活动未开始",
            isActivityOver: "活动已结束",
            isActivityPaused: "活动进度已暂停",
            isNotEligibleForActivity: "您不在可参与活动用户范围中",
            canGetAllCoupons: "可以获得所有优惠券啦!",
            canRedeemCoupons: "就可以领取优惠券了哦",
            isAvailableToGet: "可获得",
            isConsumedOrReached: "消耗 | 达到",
            ke: "颗",
            isPointsCollectionComplete: "一起来集点，集满有好礼赠送",
            isGiftToBeClaimed: "你有待领取礼品哦",
            noDataAvailable: "暂无数据",
            isIDNotAvailable: "未获取到ID",
            couponListToRedeem: "领取优惠券列表",
            unclaimedCouponsAvailable: "您还有未领取的优惠券哦！",
            notEligibleForActivity: "您当前不在可参与活动用户范围中或者活动已经结束",
            activityRestrictions: "活动参与限制",
            onlyAllowedFor: "仅限",
            availableBenefits: "可享",
            allGoalsAchieved: "您已点亮所有{star}",
            loyaltyCardPoints: "集点卡",
            zhi: "至",
            hasOwnership: "已拥有{star}",
            activityInfo: "活动说明",
            starPopBtnText: "知道了 | 立即领取",
            couponReceived: "优惠券已到账",
            inviteFriendsForGifts: "您还可以邀请好友一起参加领取礼品哦~",
            shareWithFriends: "分享好友",
            autoConvertedToCoupon: "已自动兑换成优惠券",
            promptToRedeem: "请及时领取",
            actualConsumptionNHasGiftTipYuan: "实际消费每满{symbol}{amount}（包含），完成取餐后可获赠对应数量礼品",
            actualConsumptionNHasGiftTipItems: "实际消费每满{ n }件（包含），完成取餐后可获赠对应数量礼品",
            actualConsumptionNHasGiftTipSingleItems: "实际消费满{ n }件（包含），完成取餐后可获赠对应数量礼品",
            renounceOrderFiscountToGetTheAboveRewards: "放弃本单优惠可获得上述奖励",
            additionalBenefits: "份其他权益",
            pointsRedeemableForGifts: "积分可兑换好礼",
            giftQuantitiesTips: "礼品数量以实际发放为准，发放有所延迟，请耐心等候",
            AddOn: "加购",
            gift: "贈品",
            give: "送",
            combine: "拼",
            CurrentQuantity: "当前数量",
            PendingActivation: "待生效",
            RedeemedQuantity: "已兑换数量",
            CouponClaimed: "已领取优惠券",
            Introduction: "介绍",
            TakesEffectAtMidnightTheNextDay: "隔天凌晨生效",
            IncreasedSpending: "消费增加",
            RedemptionDecrease: "兑换减少",
            RefundAndCorrectionDecrease: "退款冲正减少",
            ManualIncrease: "手动增加",
            ManualDeduction: "手动扣减",
            Addition: "增加",
            Reduction: "减少",
            TreasureReversalIncrease: "宝藏扣回增加",
            ClickHereToViewTheEeventRules: "点这里查看活动规则",
            Collect: "集",
            ThisOrderIsExpectedToEarn: "本单预计获得{n}“{m}”",
            ForgoOrderBenefitsOnlyCollect: "放弃本单优惠，仅累计“{n}”",
            noForgetSelectDiscount: "不要忘记选择您的优惠哦",
            ThisOrderCanEarn: "当前订单可获得{n}“{m}”",
            DiscountedItemsNoQualifyFor: "优惠商品不可参与集",
            points: "点",
            PromotionalPproductsCanEarn: "优惠商品可参与集",
            Discount: "惠",
            EnjoyDiscountNoAccumulation: "享受优惠，不集{n}",
            CollectPointsNoDiscount: "我要集{n},不享受优惠",
            ExplanationOfExpectedPoints: "预计可得{n}说明",
            QualifyingPaidAmountForPoints: "可获得“{n}”的实付金额",
            ItemsQualifyingForPoints: "可获得“{n}”的商品",
            GiftDetails: "礼品详情",
            sheetCoupons: "张券"
          },
          coupon: {
            HotSaleBuyNow: "热销中，速速抢购",
            Endson: "距结束",
            Only: "仅需",
            SoldOut: "已被抢",
            LimitedToNPieces: "限售 n 份",
            Untilthesalestarts: "距开抢还有",
            CouponsIncluded: "券包内含有以下券",
            PurchaseNotice: "购买须知",
            voucher: "兑换券",
            NTotal: "共{n}张",
            Grabnow: "开抢",
            agreeTo: "我已阅读并同意",
            onlyStudents: "仅支持学生购买，请先实名认证",
            PurchaseSuccessful: "购买成功",
            SenttoYourCardPack: "已发送至您的卡包",
            sendAccount: "优惠券已发放至您的账户，可至“我的-优惠券”查看",
            Distance: "距离您",
            ValidPurchase: "仅在购券门店使用",
            ApplicableStores: "所有门店适用",
            ApplicableProducts: "所有商品适用",
            Instructions: "使用说明",
            Notification: "系统提示",
            ReadAgree: "请先阅读并同意“付费券包协议”",
            Agree: "同意协议",
            Disagree: "不同意",
            exceededLimit: "已超出購買限制",
            selectStore: "请先选择活动所在门店",
            HotSale: "正在疯抢",
            StartingSoon: "即将开始",
            switchOtherstores: "暂无进行中优惠券包活动，您可切换其他门店查看",
            NoActiveEvents: "暂无活动内容，请先授权当前定位信息"
          },
          address: {
            newAddress: "新增地址",
            Recipient: "收货人",
            ImportfromWeChat: "微信导入",
            Mr: "先生",
            Ms: "女士",
            PhoneNo: "手机号",
            Autofill: "自动填写",
            Address: "地址",
            PleaseSelectYourAddress: "请选择所在地址",
            HouseNo: "门牌号",
            Tag: "标签",
            DeliveryAddress: "收货地址",
            AddNewAddress: "新增收货地址",
            ConfirmDeleteAddress: "确认删除该地址吗?",
            outRange: "该地址超出门店配送范围，您可以重新选择配送门店",
            outRangeShop: "以下地址超出【{n}】配送范围",
            Name: "名字",
            exampleRoom: "例：5号楼203室",
            SetasDefaultAddress: "设为常用地址",
            multipleAddresses: "当定位附近有多个地址时，优先使用该地址",
            DeleteAddress: "刪除地址",
            Other: "其他",
            andUse: "并使用",
            EditAddress: "编辑地址",
            FillNameplease: "填個名字呗",
            checkName: "姓名必须包含文字或字母，请重新填写",
            checkPhone: "手机号不能为空",
            enterValidphoneNumber: "请输入正确的手机号",
            addressisrequired: "地址必填哦",
            houseNorequired: "门牌号必填哦",
            CurrentlyUnabletoDeliver: "该地址暂无法配送",
            Nostoresfordelivery: "该地址附近暂无可提供配送的门店，您可选择其他地址，也可继续选择该地址",
            editOrEmpty: "编辑",
            addOrEmpty: "新增",
            Revise: "重新编辑",
            ContinueSave: "继续保存",
            AddressOutrange: "当前收货地址超出门店配送范围，如需使用该地址，可保存返回重新选择门店下单",
            PlaceOrderAgain: "重新下单",
            NotNow: "暂不使用",
            UpdatedSuccessfully: "修改成功",
            AddedSuccessfully: "添加成功",
            ImportFailed: "导入失败",
            notDeclaredPrivacyPolicy: "该功能未在隐私协议中声明",
            PhysicalStoredVCard: "實體儲值卡",
            DeliverableAddresses: "可配送至以下地址",
            CurrentLocation: "当前定位",
            UnableCurrently: "当前无法获取定位",
            RetryLocation: "重新定位",
            Reauthorize: "重新授权",
            MyDeliveryAddress: "我的收货地址",
            MyEvaluations: "我的评价",
            PartialRefunds: "部分商品退款时{n}将不退",
            DiscountApplied: "已享受折扣",
            noffset: "（其中{n}抵扣",
            NoDeliveryAddressYetGoAddOneNow: "还没有收货地址，快去添加吧~",
            ManageDeliveryAddresses: "管理收货地址",
            SelectAddress: "选择地址"
          },
          stdCommon: {
            accountException: "您的账号存在异常，请联系客服处理",
            iKnow: "我知道了"
          },
          stdMarketing: {
            myPrize: "我的奖品",
            activityRules: "活动规则",
            setTheCorrectActivityId: "请配置正确的 activityId",
            theActivityIsNotInProgress: "活动不在进行中",
            tooLateAllGone: "您来晚了，已领完",
            receivedAlready: "已领取",
            eventUnavailableAtTheCurrentTime: "当前时间活动不可参与",
            afterStart: "后 开始",
            preAfterStart: "",
            other: "其他",
            queueJumpPrivilege: "免排队特权",
            trilateralPrivileges: "三方权益",
            collecting: "领取中",
            totalStockTips: "您来晚了，已领完",
            dayStockTips: "您来晚了，今日已领完",
            weekStockTips: "您来晚了，本周已领完",
            monthStockTips: "您来晚了，本月已领完",
            totalTimesTips: "已达上限",
            dayTimesTips: "今日已达上限",
            weekTimesTips: "本周已达上限",
            monthTimesTips: "本月已达上限",
            NoPrizeInformationAvailable: "暂无奖品信息",
            SystemError: "系统异常",
            RetrieveTime: "获取时间",
            ToppingVoucher: "加料券",
            SessionVoucher: "次券",
            ParkingVoucher: "停车券",
            FreebieVoucher: "免单券",
            DeliveryVoucher: "配送费券",
            ReduceToVoucher: "减至券",
            PickUpVoucher: "提货券",
            AForBFreeCoupon: "买A赠B券",
            EventunavailableNow: "当前时间活动不可参与",
            PleaseEnterTheClaimCode: "请输入领取口令",
            EventNoStartedYet: "活动还未开始",
            TooLateEventEnded: "您来晚了，活动已经结束了",
            backHomepage: "去首页逛逛",
            DailyLimitReached: "今日已兑完",
            WeeklyLimitReached: "本周已兑完",
            MonthlyLimitReached: "本月已兑完",
            RedemptionComplete: "已兑完",
            ProductRedemptionLimitReached: "该商品兑换已达上限",
            HowToObtainARedemptionCode: "如何获取领取口令？"
          },
          stdPoint: {
            CheckLogging: "登录后查看",
            PrizeRedemptionRecord: "奖品兑换记录",
            EventRules: "活动规则",
            LimitedRedemptions: "限兑{n}份",
            NotPeriod: "未在兑换时段内",
            RedeemLogging: "登录后兑换",
            Insufficientpoints: "积分不足",
            RedemptionRecord: "兑换记录",
            Norecords: "暂无兑换记录",
            View: "去查看",
            ObtainedTime: "获得时间",
            ConfirmRedemption: "确认兑换",
            Confirmtouse: "确认使用",
            Toredeem: "兑换",
            Confirm: "确认兑换",
            RedemptionSuccessful: "兑换成功",
            RedemptionFailed: "兑换失败",
            ViewGiftRedemptionRecords: "查看礼品兑换记录",
            Continue: "继续兑换",
            Gotit: "知道了",
            Redeeming: "兑换中",
            CouponDescription: "优惠券说明",
            RedemptionRules: "兑换规则",
            back: "返回"
          },
          card: {
            TrialCard: "体验卡",
            MoreServices: "更多服务",
            CardList: "权益卡列表",
            BuyHistory: "购买记录",
            UsageRules: "使用规则",
            FAQ: "常见问题",
            Redeem: "兑换",
            UseBenefitsNow: "前往使用权益",
            TotalSaved: "累计已省",
            GroupCard: "集团会员卡还可在关联品牌下享受权益",
            paidmembershipstudents: "当前付费会员仅学生可购买，请前往认证",
            Periodic: "提示：周期权益待体检卡失效后再进行发放",
            CardAgreement: "《付费权益卡协议》",
            giveFriends: "赠送好友",
            agreeMembershipAgreement: "請勾選付費會員協議",
            RenewNow: "立即续费",
            NotAvailable: "暂不可购买",
            RenewableAfter: "{n}后可续费",
            BuyAgain: "再次购买",
            OfficiallyLaunched: "正式开通",
            Renew: "续费",
            GifttoThem: "送给TA",
            PaidBenefitsCard: "付费权益卡",
            AnErrorOccurred: "出错了",
            StoreNoAvailable: "该门店暂无可售权益卡，请切换门店",
            FreeExperience: "免费体验",
            StudentsOnly: "仅学生可购买",
            BoundasStudent: "已绑定，学生",
            SwitchStore: "切换门店",
            day: "天",
            Usable: "可使用",
            Expired: "已过期",
            Saved: "已节省",
            PendingGift: "待赠送",
            Gifting: "赠送中",
            Gifted: "已赠送",
            GiftExpired: "赠送超时",
            CardName: "卡名称",
            Experience: "体验",
            Valid: "有效",
            Days: "天数",
            GiftTime: "赠送时间",
            UseItYourself: "自己使用",
            CancelGift: "取消赠送",
            NoBenefitsCard: "暂无权益卡",
            MyBenefitsCard: "我的权益卡",
            GiftBenefitsCard: "赠送权益卡",
            PleaseConfirm: "请确认",
            cancelConfirm: "是否取消赠送当前权益卡?",
            activateCard: "是否激活当前权益卡，自己使用？",
            ActivationSuccessful: "激活成功",
            BenefitsCardList: "权益卡列表",
            PleaseInput: "请输入",
            RedemptionCode: "兑换码",
            CardNumber: "卡号",
            Key: "密钥",
            CardPIN: "卡密",
            Instructions: "说明",
            Entercardnumber: "输入实体储值卡卡片上的卡号和卡密进行绑卡",
            EnterthePIN: "输入实体储值卡卡片上的卡密进行绑卡",
            Afterbindingcard: "卡片绑定后，该实体储值卡的充值消费退款等流水只记录实体储值卡账户的流水（手机号仅作身份识别）",
            Bind: "绑定",
            exchange: "兑换",
            CodeInformationNotRecognized: "未识别到码信息",
            redemptionSuccessful: "恭喜您，兑换成功！",
            experienceBenefits: "可以体验一下超值权益哦～",
            BenefitsCardRedemption: "权益卡兑换",
            FreeTrial: "免费体验"
          },
          stdPointMall: {
            details: "明细",
            unauthorizedLocationNoStore: "未授权定位，获取门店失败",
            expirationReminder: "到期提醒",
            awayFormYou: "距您",
            pointsExpireTips: "{m}将于{n}到期",
            congestionAheadPleaseTryAgainLater: "亲，前方出现拥堵，请稍后重试！",
            tryAgain: "重新试试",
            loadingFrantically: "玩命加载中...",
            retailMall: "零售商城",
            integralMall: "积分商城",
            originalPrice: "原价{n}",
            leftStock: "剩余",
            leftStockAfterItems: "件",
            redeemed: "已兑换",
            redeemedAfterItems: "件",
            countdownToGrabAndRedeem: "倒计时抢购兑",
            saleTime: "售卖时间",
            timeDay: "天",
            productReview: "商品评价",
            productDetails: "商品详情",
            redemptionStartsSoon: "即将开始兑换",
            activateYourCardNow: "您还未开卡，点击前往开卡",
            membershipLevelInsufficient: "会员等级不满足",
            premiumMember: "付费会员",
            notEnoughParticipationCriteriaTips: "很抱歉，您当前不满足参与条件～",
            dailyRedemptionLimitReached: "当日已达到兑换上限",
            youReachedRedemptionLimit: "您已达到兑换上限",
            promotionEnded: "活动结束",
            goodsIsEmptyTips: "当前{n}商品走丢啦~",
            confirmRedemption: "是否确认兑换？",
            redemptionDetails: "兌換詳情",
            benefitsUseTips: "权益卡使用规则详见兑换详情页",
            iHaveReadAndAgree: "我已阅读并确认同意",
            paidBenefitsCardAgreement: "付费权益卡协议",
            isThisAGift: "要作为礼物赠送吗？",
            notAGift: "不赠送",
            useMyself: "自己使用",
            giftToAFriend: "赠送给好友",
            friendUse: "好友使用",
            friendMustRegisterToClaimTheGift: "赠送给好友时，好友需注册会员后进行领取",
            pleaseCheckTheTtermsAndConditions: "请先勾选须知",
            orderConfirmation: "订单确认",
            confirmRedemptionTips: "确认兑换",
            addressList: "选择收货地址",
            wxExportAddress: "微信导入地址",
            addNewShippingAddress: "新增收货地址",
            addressName: "收货人",
            gettingYourAddressRequiresLocationPermission: "获取地址需要您的位置信息授权",
            refundDetail: "退款详情",
            addImage: "添加图片",
            SelectRefundItems: "选择退款商品",
            detailedRefundReasonsWwillHelpTheStoreProcessFaster: "补充详细退款原因，有利于门店更快帮您处理",
            UploadImagesTips: "最多可上传五张图片，每张图片不超过5M",
            refundRules: "退款规则",
            refundRules1: "全部退款时，退款金额为整单实付金额（含包装费、配送费），优惠券原路返回；",
            refundRules2: "选择部分退款时，退款金额为退款商品按比例分摊优惠金额及对应的包装费，不退配送费；",
            refundRules3: "参与商户营销活动的订单只能进行全部退款",
            refundRules4: "商品发生退款时，订单中商品全部退款完成后返还",
            selectRefundReason: "请选择退款原因",
            noRecordsAvailable: "暂无记录",
            noMore: "没有更多了哟",
            pullUpToLoadMore: "上拉加载更多",
            noLogisticsInfo: "暂无物流信息~",
            copySuccess: "复制成功",
            validityPperiodCalculating: "有效期正在计算中",
            voucherCode: "兑换码",
            Recycled: "已回收",
            redemptionTime: "兑换时间",
            UsageGuidelines: "使用须知",
            UsageConditions: "使用条件",
            PromotionType: "优惠形式",
            UsagePeriod: "使用时段",
            DailyUsageLimit: "单日使用限制",
            SingleOrderUsageLimit: "单笔订单使用限制",
            EligibleProducts: "适用商品",
            Shareability: "是否与其他优惠共享",
            ApplicableScenarios: "适用场景",
            RedeemAgain: "再次兑换",
            ViewNow: "立即查看",
            MyAccount: "我的账户",
            statusTextBefore1: "已放入账户，去",
            ba: "吧",
            RedeemedsuccessfullyHurryTo: "兌換成功，趕緊去",
            GiftedToFriendTo: "已赠送给好友，去",
            BenefitCardGiftList: "权益卡赠送列表",
            ExchangeDetails: "兑换信息",
            ShippingDetails: "物流信息",
            AwaitingPayment: "待支付",
            AwaitingDispatch: "待发货",
            AwaitingDelivery: "待收货",
            Finished: "已完成",
            DeliveredTo: "商品配送至",
            PleaseEnterTheDeliveryAddress: "请填写配送地址",
            ShippingCost: "快递费",
            PleaseSelectAnAddress: "请选择地址",
            RedemptionNo: "兑换单号",
            RedemptionStatus: "兑换状态",
            Use: "使用",
            LogisticsCompany: "物流公司",
            LogisticsNumber: "物流单号",
            ConfirmCancelRedemptionTips: "确认取消兑换？所消耗{n}将退还",
            receiptGoodsTips: "确认收到货了吗",
            DeliveryConfirmed: "收货成功",
            goPay: "继续支付",
            Refund: "退款",
            EnterAddress: "填写地址",
            NoCurrentEventWinningsRecordedYet: "暂时还没有活动中奖记录",
            PrizeDetails: "奖品详情",
            RightsExplanation: "权益说明",
            ShippingNumber: "运单号",
            AwardDate: "获奖时间",
            PrizeSource: "奖品来源",
            MysteryBoxDraw: "盲盒抽奖",
            EntitlementDetails: "权益详情",
            PrizeDetails2: "实物奖品详情",
            StoredValueBalance: "{n}元储值余额",
            ClaimResult: "“领取结果",
            DispatchInProgress: "努力发放中...",
            CheckIn: "签到",
            nLuckyDraw: "{n}抽奖",
            PleaseSelectAtLeastOneItem: "请选择至少一件商品"
          },
          stdUser: {
            warning: "注意",
            tip: "提示",
            rtnIndex: "返回首页",
            noSupport: "暂不支持，请联系品牌客服",
            noData: "暂无数据",
            noMoreData: "没有更多了",
            confirm: "确定",
            thinkAgain: "再想想",
            cancel: "取消",
            operateFail: "操作失败",
            integral: "积分",
            fetchError: "请求失败，请稍候再试试",
            authSuccess: "授权成功",
            bindSuccess: "绑定成功",
            bindFail: "绑定失败",
            invalidTo: "无效的跳转",
            saveSuccess: "保存成功",
            saveFail: "保存失败",
            growthValue: "成长值",
            loading: "加载中",
            ok: "好的",
            readAndAgree: "我已阅读并同意",
            copy: "复制",
            iGotIt: "我知道了",
            selectAll: "全选",
            wxUser: "微信用户",
            aliUser: "支付宝用户",
            ttUser: "抖音用户",
            blackUserTip: "您的账号操作异常,请联系客服处理",
            unrecognizedCode: "未识别到码信息",
            all: "全部",
            unit: {
              yuan: "元",
              zhang: "张",
              times: "次",
              year: "年",
              month: "月",
              day: "日",
              hour: "时",
              minutes: "分",
              second: "秒"
            },
            personal: {
              title: "个人资料",
              pleaseInput: "请输入",
              nickName: "昵称",
              inputNickName: "请输入昵称",
              gender: "性别",
              male: "男",
              female: "女",
              phoneNum: "手机号",
              replacePhone: "更换",
              pleaseAuth: "请授权手机号",
              changeMobileTip: "重新授权将清除当前已绑定的手机号，是否确认操作？",
              birthday: "生日",
              selectBirthday: "请选择生日",
              birthdayPrivileges: "完善生日，不错过惊喜",
              notModified: "填写完不可修改",
              onlyFillInOnce: "每年仅可填写一次",
              address: "地址",
              selectAddress: "请选择地址",
              save: "保存",
              logout: "退出登录",
              confirmLogoutTitle: "确定退出登录？",
              logoutTip: "退出后将无法查看订单相关信息",
              confirmLogout: "确定退出",
              privilegesGiftDialogTitle: "赠送您以下权益",
              toSee: "查看",
              mustBeNumber: "必须为数字",
              gift: "赠送",
              canExchange: "可在积分商城兑换好礼",
              today: "今日",
              thisMonth: "本月",
              thisYear: "今年",
              phoneChangeTip: "您{m}还可更换{n}次，确定要更换手机号吗？",
              notAllowUnderageTip: "根据您的生日信息，您未满18岁，暂不支持设置"
            },
            accountMgmt: {
              title: "账号管理",
              switchAccount: "切换账号",
              writeOffAccount: "注销账号",
              writeOffTip: "注销后无法恢复，请谨慎操作",
              confirmLogoutTitle: "确定退出登录？",
              logoutTip: "退出后将无法查看订单相关信息",
              confirmLogout: "确定退出",
              logoutFail: "退出登录失败",
              logoutSuccess: "退出登录成功",
              pwdSet: "设置储值支付密码",
              pwdMod: "修改储值支付密码"
            },
            logOff: {
              title: "账号注销",
              descTitle_1: "您将注销账号：",
              descTitle_2: "，请仔细阅读以下说明：",
              descItemTitle_1: "一、账号注销条件",
              descItemTip_11: "1.账号内没有未完成的订单；",
              descItemTip_12: "2.申请注销的账号在当前品牌下无未激活或赠送中的礼品卡；",
              descItemTitle_2: "二、账号注销效果",
              descItemTip_21: "1.账号一旦被注销将无法再找回或恢复，您将无法再登录、使用已注销的账号,也无法获得已注销账号的信息和数据(包括手机号、头像、称谓、生日、性别等)；",
              descItemTip_22: "2.账号下曾获得的会员权益、优惠券、积点、活动资格及其他相关虚拟权益视为您自行放弃,无法继续使用；",
              descItemTip_23: "3.请您理解并同意，我们无法协助您重新恢复前述服务。请您在提交注销申请前，",
              descItemTip_24: "务必对您账号内的虚拟资产进行处理。",
              writeOffTip: "账号一旦注销，账户资产将无法恢复",
              agreement: "注销协议",
              confirmNext: "已确认，下一步",
              selectReasonTitle: "选择注销的原因",
              selectReasonTip: "您的反馈会帮助我们做的更好",
              pleaseInputReason: "请填写注销原因",
              confirmLogOff: "确定注销",
              applySubmit: "注销申请已提交",
              applyResTip_1: "账号将于",
              applyResTip_2: "天后",
              applyResTip_3: "正式注销，在此之前您可撤销注销",
              logOffConfirmTitle: "确定要注销当前账号？",
              logOffConfirmTip: "注销后您的信息和资产将被清空且无法恢复",
              logOffConfirmTipWithCoolingOffPeriod: "注销后你的消息和资产将被清空且无法恢复，当前注销账号具有{n}天冷静期，冷静期内可主动取消注销",
              logOffSuccess: "账号注销成功",
              logOffFail: "账号注销失败",
              notCanLogOff: "存在未完成的订单，暂不支持注销",
              frozenTitle: "当前账号处于注销冷冻期",
              continueLogOff: "继续注销",
              revokeCancel: "撤销注销",
              revokeFail: "撤销失败",
              revokeSuccess: "注销已撤回",
              pleaseSelectReason: "请选择注销原因",
              reason1: "服务不满意",
              reason2: "产品不满意",
              reason3: "注册了新账号",
              reason4: "附近没有门店",
              reason5: "营销信息骚扰",
              other: "其他"
            },
            accountSwitch: {
              title: "切换账号",
              nowMobilePhone: "当前登录手机号：",
              tips: "切换其他账号后，当前登录的账号将退出！\n新手机号若未注册，将自动注册为新账号",
              confirmSwitch: "确认切换",
              switchSuccess: "账号切换成功",
              switchFail: "账号切换失败",
              iGotIt: "我知道了",
              switchLimit: "今日切换次数已达上限"
            },
            mobileVerifyCode: {
              mobile: "手机号",
              verifyCode: "验证码",
              getVerifyCode: "获取验证码",
              getVerifyCodeFailed: "验证码发送失败，请稍候重试",
              getVerifyCodeSuccess: "验证码发送成功",
              mobileEmpty: "请输入手机号",
              mobileInvalid: "请输入正确的手机号",
              verifyCodeEmpty: "请输入验证码",
              reGet: "后重发",
              pleaseEnterMobileAndVerifyCode: "请输入手机号和验证码"
            },
            assets: {
              balance: "余额",
              point: "积分",
              coupon: "优惠券",
              giftCard: "礼品卡",
              storeValueCard: "储值卡",
              equityCard: "权益卡",
              physicalCard: "实体储值卡",
              medal: "勋章"
            },
            assetsMove: {
              title: "资产迁移",
              step1: "选择方式",
              step2: "填写账号",
              step3: "选择资产",
              step4: "迁移结果",
              next: "下一步",
              upperLimit: "您已达迁移次数上限",
              confirm: "确认迁移",
              record: "迁移记录",
              moveNeedKnow: "迁移须知",
              moveTip_1: "1. 资产将迁移至您已更换的新手机号，需将以前账号的资产迁移至新账号；",
              moveTip_2: "2. 因为涉及到资产相关，请您谨慎操作！",
              selectMoveType: "选择迁移方式",
              assetsMoveOut: "资产迁出",
              assetsMoveOutTip: "将本账号的资产迁移至其他账号",
              assetsMoveIn: "资产迁入",
              assetsMoveInTip: "将其他账号的资产迁移至本账号",
              pleaseSelectMoveType: "请选择迁移方式",
              nowAccountAssets: "当前登录账号资产",
              nowAccount: "当前登录账号",
              receiveAccount: "接收账号",
              transferAccount: "转出账号",
              pleaseInputPhone: "请填写手机号",
              selectNowAssets: "选择当前登录账号资产",
              assetsToNew: "选中的资产将迁出至账号",
              select: "选择",
              accAssets: "账号资产",
              assetsToNow: "选中的资产将迁入至当前登录账号",
              pleaseSelectAssets: "请选择资产",
              out: "迁出",
              in: "迁入",
              success: "成功",
              fail: "失败",
              assets: "资产",
              result_tip_1: "当前登录账号",
              result_tip_2: "已迁出至账号",
              result_tip_3: "账号",
              result_tip_4: "已迁入至当前登录账号",
              dialogTitle_1: "确定要迁出资产吗？",
              dialogTitle_2: "确定要迁入资产吗？",
              dialogTip: "将账号",
              dialogTip_1: "资产迁出到账号",
              dialogTip_2: "资产迁入到账号",
              outAccount: "迁出账号"
            },
            assetsMoveRecords: {
              title: "资产迁移记录",
              changeAccount: "变动账户",
              time: "时间"
            },
            user: {
              reGet: "再获得",
              growthValueUpgrade: "可升级为",
              beyondLevel: "您已超越该等级",
              stillPoor: "还差",
              raisedToLevel: "可升至该等级",
              memberExpired: "已过期",
              willBe: "将于",
              failure: "失效",
              myAbility: "我的功能",
              perfectInfoTip: "完善信息可获得奖励",
              technicalSupport: "企迈提供技术支持",
              welcomeYou: "欢迎您",
              toLoginTip: "登录会员尊享多重好礼",
              login: "登录",
              toLogin: "去登录",
              loginNow: "立即登录",
              notUnlocked: "未解锁",
              allEquity: "全部权益",
              nowToMaxLevel: "恭喜你，已达到最高等级",
              maxLevel: "最高等级",
              unlock: "已解锁",
              toBeUnlocked: "待解锁",
              canEnjoy: "可享",
              itemEquity: "项权益",
              nowLevel: "当前等级",
              myAssets: "我的资产",
              expiration: "到期",
              toOpen: "去开通",
              seeEquity: "查看权益",
              renewNow: "立即续费",
              toLoginBoot: "您还没有登录哦",
              myOrder: "我的订单",
              seeAll: "查看全部",
              noSoonExpiredPoints: "近7天内无积分过期",
              send: "送",
              expName: "经验值",
              double: "翻倍",
              discountForConsumption: "消费享折扣",
              myMedal: "我的勋章",
              noContactPhone: "未配置联系电话",
              noCustomerServicePhone: "未配置客服电话",
              levelStageCompleted: "您已完成此阶段",
              levelUpToN: "升级为{n}",
              levelUpToNext: "升级为下一等级",
              petUnlockNoticeN: "已解锁第{n}只萌宠",
              adoptionQualification: "领养资格",
              adoptionCompleted: "恭喜你已完成全部",
              petAdoption: "萌宠领养"
            },
            memberCode: {
              title: "会员码",
              seeNum: "查看数字",
              hideNum: "隐藏数字",
              memberUpdateTip: "{n}秒后自动更新，请在店内消费使用",
              useWxPay: "使用微信支付",
              useAliPay: "使用支付宝支付",
              SelectRegion: "选择地区",
              antiScreenshotTips: "会员码仅限门店消费时出示给店员扫码获取会员权益，截屏无效，请不要将会员码及数字发送给他人，感谢惠顾"
            },
            coupon: {
              list: "{n}列表",
              subscribeTips: "开启{n}到期/到账提醒",
              subscribeBtn: "立即订阅",
              cancelSubscribeBtn: "取消订阅",
              toGift: "送好友",
              toUse: "去使用",
              historyCoupon: "历史券",
              historyTitle: "历史{n}",
              batchGift: "批量赠送",
              giftRecord: "赠送记录",
              exchangeCoupon: "兑换{n}",
              codeEmpty: "请输入兑换码",
              keyEmpty: "请输入秘钥",
              confirmExchange: "确认兑换",
              exchangeSuccessDialogTitle: "{n}兑换成功",
              continueExchange: "继续兑换",
              seeGiftRecords: "查看赠送记录",
              selectFriend: "选择好友",
              confirmGift: "确定赠送",
              confirmGiftXToFriend: "确定赠送{n}张{m}给好友？",
              confirmGiftToFriend: "确定赠送该张{m}给好友？",
              giftToFriend: "赠送好友",
              pleaseSelectCoupon: "选择要赠送的{n}",
              receiveCoupon: "领取优惠券",
              selectGiftCover: "选择赠送封面",
              selectGiftBlessings: "选择赠送祝福语",
              currentBlessing: "送你一份小心意，快来领取吧～",
              receiveImmediately: "立即领取",
              goToUse: "前往使用",
              toYourAccount: "优惠券已成功领入你的账户",
              goToView: "前往查看",
              quickReceive: "你的好友送你优惠券啦，速速领取！",
              wantToSayToYou: "你的好友送你优惠券啦，TA想对你说",
              wantToSayToHim: "送好友优惠券啦，你想对TA说",
              noCoupon: "您暂时还没有优惠券~",
              noCanGiftCoupon: "您暂时还没有可赠送的{n}~",
              subscribeTipsDialogTitle: "{n}提醒",
              subscribeTips1: "1、{n}提醒将以服务通知的形式进行推送， 单次推送后需再次订阅",
              subscribeTips2: "2、提醒分为{n}到账提醒和优惠券到期提醒",
              subscribeTips3: "3、为了提高订阅效率，建议勾选“保持以上选择，不再询问”",
              applyStoresTitle: "适用门店",
              selectStoreApplyGoods: "选择商品适用门店",
              applyGiftCards: "适用礼品卡",
              noApplyGiftCards: "暂无适用的礼品卡",
              applyRightsCards: "适用权益卡",
              noApplyRightsCards: "暂无适用的付费权益卡",
              noApplyStores: "当前城市无适用门店",
              applyGoods: "适用商品",
              mallApplyGoods: "商城适用商品",
              cancelGift: "取消赠送",
              cancelGiftTip: "是否确定取消赠送？",
              cancelGiftSuccess: "取消赠送成功",
              receiveSuccess: "领取成功",
              openSettingBtn: "去设置",
              codeUpdateTip: "{n}秒后自动更新",
              giftingCouponCount: "{n}张赠送中",
              batchGiftTips: "请选中可赠送优惠券",
              used: "已使用",
              invalid: "已失效",
              redeemCode: "兑换码",
              redeemCodeWithKey: "兑换码+密钥",
              pleaseEnterRedeemCode: "请输入兑换码",
              pleaseEnterKey: "请输入密钥",
              invalidRedeemCode: "兑换码错误",
              receiveCouponNeedAuthLocation: "领取优惠券需要您授权地址位置",
              confirmRedeemCoupon: "券码兑换成功后，可在下单时使用，是否确认兑换？",
              exchangeSuccess: "兑换成功",
              redemptionCode: "核销码",
              getCodeError: "获取核销码失败",
              freeExpansion: "免费膨胀",
              maxN: "最高{n}",
              giving: "赠送中",
              given: "已赠送",
              noCouponsGiving: "您暂时没有赠送中的{n}",
              noCouponsGiven: "您暂时没有已赠送的{n}",
              usedFilterNote: "仅展示近3个月内已使用券",
              expired: "已过期",
              expiredFilterNote: "仅展示近3个月内已过期券",
              recycled: "已回收",
              recycledFilterNote: "仅展示近3个月内已回收券",
              usageRules: "使用规则",
              availableEverywhere: "全场景可用",
              dineIn: "堂食",
              takeout: "外卖",
              checkout: "买单",
              pickup: "自提",
              storeDelivery: "门店（快递）",
              limitN: "限{n}",
              day: "{n}天",
              hour: "{n}小时",
              minutes: "{n}分钟",
              second: "{n}秒",
              expireCountdown: "距过期仅剩{n}",
              unavailableInTime: "当前时段不可用",
              unavailableInChannel: "当前渠道不可用",
              expansionAmountError: "膨胀金额异常",
              totalCount: "共{n}张",
              leftCount: "剩{n}张",
              merchantCoupon: "商家券",
              activityCoupon: "活动券",
              inflatedCoupon: "膨胀券",
              latestAcquired: "最新获得",
              expiringSoon: "即将到期",
              allCoupons: "全部优惠券",
              effective: "已生效",
              ineffective: "未生效",
              allScenes: "全部场景",
              delivery: "外卖",
              payment: "买单",
              friendCanceled: "您的好友已取消赠送",
              alreadyReceived: "您来晚啦，{n}已被他人领取",
              couponTimeout: "{n}已超时退回啦，下次早点领取哦",
              pageExpired: "领取页面已过期",
              receiveNow: "立即领取",
              goToAccount: "前往账户查看",
              goToMiniProgram: "去小程序逛逛",
              friendReceived: "您的好友{n}领取了{m}",
              friendNotReceivedTip: "您的好友还未领取，24小时未领取将自动退回哦",
              cancelGiftReturned: "您已取消赠送，{n}已退回至您的账户",
              friendTimeoutReturned: "您的好友超时未领取{n}已退回至您的账户",
              selectBrandTitle: "选择去使用的品牌",
              brandNoMiniApp: "品牌名称未配置小程序",
              openSubscribeGuide: "请按以下操作开启消息提醒",
              cancelSubscribeTitle: "取消订阅提醒",
              cancelSubscribeContent: "取消订阅后，将不再收到消息提醒，确定取消吗？",
              confirmCancel: "确定取消",
              cancelCancel: "不取消了",
              closeSubscribeGuide: "请按以下操作关闭消息提醒",
              allPaidRightsCard: "全部付费权益卡",
              specifiedPaidRightsCard: "指定付费权益卡",
              allN: "全部{n}",
              specifiedGiftCard: "指定{n}",
              storedValue: "储值余额",
              anyAmount: "任意金额支付",
              fullAmount: "整单金额支付",
              remainingCount: "剩余{m}次，共{n}次",
              id: "优惠券ID",
              applyBrand: "适用品牌",
              applyCard: "适用卡片",
              viewCard: "查看卡片",
              applyN: "适用{n}",
              applyStore: "适用门店",
              viewStore: "查看门店",
              storeGoods: "门店商品",
              viewGoods: "查看适用商品",
              mallGoods: "商城商品",
              applyChannel: "适用渠道",
              applyScene: "适用场景",
              validityPeriod: "有效期",
              usePeriod: "适用时段",
              disabledTimes: "不可用时间",
              additionalGoods: "加料商品",
              additionalGoodsYes: "参与优惠",
              additionalGoodsNo: "不参与优惠",
              restrictedPay: "限制支付方式",
              paymentMethod: "是否整单使用指定支付方式支付",
              source: "优惠券来源",
              description: "优惠券说明",
              usageCount: "核销次数",
              verificationInfo: "核销信息",
              verificationBrand: "核销品牌",
              verificationStore: "核销门店",
              orderNumber: "订单号",
              verificationCodeTitle: "核销码",
              fetchVerificationCodeFailed: "获取核销码失败",
              yourFriend: "你的好友",
              receivedOnDate: "{n}领取"
            }
          }
        }
      };
      var c = o("^[0-9]+"),
        l = o("^[A-Za-z0-9_]+"),
        u = {},
        h = {};

      function p(e, t) {
        if (!t) return [e];
        var i = u[e];
        return i || (i = function (e) {
            for (var t = [], i = 0, n = ""; i < e.length;) {
              var o = e[i++];
              if ("{" === o) {
                n && t.push({
                  type: "text",
                  value: n
                }), n = "";
                var r = "";
                for (o = e[i++]; void 0 !== o && "}" !== o;) r += o, o = e[i++];
                var s = "}" === o,
                  a = c.test(r) ? "list" : s && l.test(r) ? "named" : "unknown";
                t.push({
                  value: r,
                  type: a
                })
              } else "%" === o ? "{" !== e[i] && (n += o) : n += o
            }
            return n && t.push({
              type: "text",
              value: n
            }), t
          }(e), u[e] = i),
          function (e, t) {
            var i = [],
              n = 0,
              o = r(t) ? "list" : s(t) ? "named" : "unknown";
            if ("unknown" === o) return i;
            for (; n < e.length;) {
              var a = e[n];
              switch (a.type) {
                case "text":
                  i.push(a.value);
                  break;
                case "list":
                  i.push(t[parseInt(a.value, 10)]);
                  break;
                case "named":
                  "named" === o ? i.push(t[a.value]) : console.log("Type of token " + a.type + " and format of value " + o + " do not match!");
                  break;
                case "unknown":
                  console.log("Detect unknown type of token!")
              }
              n++
            }
            return i
          }(i, t)
      }

      function d(e, t) {
        if (!s(e)) return;
        var i = h[t];
        return i || (i = function (e) {
          function t(e) {
            n(), r && s.push(r), r = f(e)
          }

          function i() {
            n();
            var e = "string" === r.type ? "__mpx_str_" + r.value.join("") : r.value;
            (r = s.pop()).push(e)
          }

          function n() {
            (a = a.trim()) && r.push(a), a = ""
          }
          var r = f(),
            s = [],
            a = "",
            c = 0;
          if (o("^[^[]]+$").test(e)) return e.split(".");
          for (; c < e.length;) {
            var l = e[c];
            "string" === r.type ? r.mark === l ? i() : r.push(l) : o("['\"[]").test(l) ? t(l) : "]" === l ? i() : "." === l || "+" === l ? (n(), "+" === l && r.push(l)) : a += l, c++
          }
          return n(), r.value
        }(t), h[t] = i), g(e, i)
      }

      function g(e, t) {
        for (var i = e, n = t.length, s = 0; s < n; s++) {
          var a, c = t[s];
          if (!i) break;
          if (r(c)) a = g(e, c);
          else if (o("^__mpx_str_").test(c)) i = c.replace("__mpx_str_", "");
          else if (o("^[0-9]+$").test(c)) i = +c;
          else {
            if ("+" === c) {
              i += g(e, t.slice(s + 1));
              break
            }
            a = c
          }
          void 0 !== a && (i = i[a])
        }
        return i
      }

      function f(e) {
        var t = [];
        return {
          mark: e,
          type: o("['\"]").test(e) ? "string" : "normal",
          value: t,
          push: function (e) {
            t.push(e)
          }
        }
      }

      function m(e, t, i, n, o) {
        var r = y(e, t, i, n);
        if ("string" == typeof r) return function (e, t) {
          return p(e, t).join("")
        }(r, o);
        return n
      }

      function y(e, t, i, n) {
        for (var o = [t, i], r = 0; r < o.length; r++) {
          var s = v(e, o[r], n);
          if (a(s)) return s
        }
      }

      function v(e, t, i) {
        if (e && e[t] && i) {
          var n = d(e[t], i);
          return null == n && (n = e[t][i]), n
        }
      }

      function _(e) {
        return e || n || {}
      }

      function b(e, t) {
        var i = e.split("|");
        if (!i[t = function (e, t) {
            if (e = Math.abs(e), 2 === t) return e ? e > 1 ? 1 : 0 : 1;
            return e ? Math.min(e, 2) : 0
          }(t, i.length)]) return e;
        return i[t].trim()
      }
      e.exports = {
        t: function (e, t, i, n, o) {
          return m(_(e), t, i, n, o)
        },
        tc: function (e, t, i, n, o, r) {
          return b(m(_(e), t, i, n, r), o)
        },
        te: function (e, t, i, n) {
          return function (e, t, i) {
            return a(v(e, t, i))
          }(_(e), t, n)
        },
        tm: function (e, t, i, n) {
          return y(_(e), t, i, n)
        }
      }, i.g.i18n || (i.g.i18n = {
        locale: "zh-CN",
        fallbackLocale: "zh-CN",
        messages: _(),
        methods: e.exports
      })
    }
  },
  function (e) {
    var t;
    t = 0, e(e.s = t)
  }
]);