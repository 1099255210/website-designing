import { defineStore } from 'pinia'
import { ref } from 'vue'

export const userInfoStore = defineStore("user", {
  state: () => {
    return {
      userName: "登录",
      userEmail: "点击左侧圆点登录",
      subtitle: "点击左侧圆点登录",
      loginStatus: 0,
    }
  },
  actions: {
    setName(arg) {
      this.userName = arg;
    },
    setEmail(arg) {
      this.userEmail = arg;
    },
    setSub(arg) {
      this.subtitle = arg;
    },
    setLoginStatus(arg) {
      this.loginStatus = arg;
    }
  }
})