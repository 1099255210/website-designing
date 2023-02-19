import { defineStore } from 'pinia'
import { ref } from 'vue'

export const userInfoStore = defineStore("userInfo", {
  state: () => {
    return {
      userName: "登录",
      userEmail: "点击左侧圆点登录",
      subtitle: "点击左侧圆点登录",
      loginStatus: 0,
      short: "",
    }
  },
  actions: {
    setStatus(userName, userEmail, subtitle, loginStatus, short) {
      this.userName = userName;
      this.userEmail = userEmail;
      this.subtitle = subtitle;
      this.loginStatus = loginStatus;
      this.short = short;
    },
  },
  persist: true,
})