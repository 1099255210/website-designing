<script setup>
import axios from 'axios'
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
</script>

<script>
export default {
  data () {
    return {
      message: 'NULL',
    }
  },
  methods: {
    async sub(credentials) {
      const res = await axios.post('/api/login', credentials)
      console.log(res['data'])
      this.message = res['data']
    }
  }
}
</script>

<template>
  <div class="contain">
    <FormKit
      type="form"
      id="login"
      @submit="sub"
    >
      <h1>登录</h1>
      <br>
      <p>请输入账号和密码</p>
      <br>
      <FormKit
        type="text"
        name="userName"
        label="用户名"
      />
      <FormKit
        type="text"
        name="userPwd"
        label="密码"
      />

    </FormKit>
  </div>
</template>