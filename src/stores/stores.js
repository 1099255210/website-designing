import { defineStore } from 'pinia'
import { ref } from 'vue'

export default defineStore('user', ()=> {
  const userName = ref('')
  const loginState = ref(0)
  const avatar = ref('')
  return userName
})