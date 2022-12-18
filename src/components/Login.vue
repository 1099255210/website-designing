<!-- <template>
  <form method="post" action="http://localhost:2145/login">
    <input type="text" name="userName">
    <input type="password" name="userPwd">
    <input type="submit" value="login">
  </form>
</template> -->

<script setup>
import axios from 'axios'
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
</script>

<script>
export default {
  data () {
    return {
      message: '',
    }
  },
  methods: {
    async sub(credentials) {
      const res = await axios.post('/api/login', credentials)
      console.log(res['data'])
      this.message = res['data']['msg']
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
    <div class="hint">{{message}}</div>
  </div>
</template>

<style scoped>

.hint {
  color: red;
  font-size: small;
}

</style>