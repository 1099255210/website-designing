import { defineStore } from 'pinia'
import { ref } from 'vue'

export const userInfo = defineStore("user", {
  state: () => {
    return {
      userName: "登录",
      userEmail: "点击左侧圆点登录",
      subtitle: "点击左侧圆点登录",
      loginStatus: 0,
    }
  }
})