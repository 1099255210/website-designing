<script setup>
import axios from "axios";
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";
</script>

<script>
export default {
  data() {
    return {
      message: "",
      valid: false,
      showPwd: false,
      userName: "",
      userPwd: "",
      userPwdConfirm: "",
      userEmail: "",
      loginornot: true,
      rules: {
        email: [
          (v) => !!v || "必须填写邮箱",
          (v) => /.+@.+/.test(v) || "邮箱无效",
        ],
        name: [
          (v) => !!v || "必须填写用户名",
          (v) => v.length <= 20 || "用户名长度最大为20",
        ],
        pwd: [
          (v) => !!v || "必须填写密码",
          (v) => v.length >= 6 || "密码长度必须大于等于6",
        ],
        pwdVerify: [(v) => v == this.userPwd || "密码不一致"],
      },
    };
  },
  methods: {
    login() {
      const data = { userName: this.userName, userPwd: this.userPwd };
      console.log(data);
      const res = axios.post("/api/login", data);
      this.message = res["data"]["msg"];
    },
    regist() {
      const data = { userName: this.userName, userPwd: this.userPwd };
      console.log(data);
      const res = axios.post("/api/regist", data);
      this.message = res["data"]["msg"];
    },
    getImageUrl(name) {
      return new URL(`../assets/${name}`, import.meta.url).href;
    },
  },
};
</script>

<template>
  <v-card>
    <v-img
      class="align-end text-white"
      height="190px"
      :src="getImageUrl('login-img.jpg')"
      cover
    >
      <v-card-text>
        <p class="text-h4">&nbsp;电子商务海报智能设计平台</p>
      </v-card-text>
    </v-img>
    <v-card-text>
      <v-btn-toggle v-model="loginornot" color="blue-grey-darken-2">
        <v-btn :value="true">登录</v-btn>
        <v-btn :value="false">注册</v-btn>
      </v-btn-toggle>
    </v-card-text>
    <v-card-text>
      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
          variant="outlined"
          v-model="userName"
          :counter="20"
          :rules="rules.name"
          label="用户名"
          required
        ></v-text-field>

        <v-text-field
          variant="outlined"
          v-model="userPwd"
          :type="showPwd ? 'text' : 'password'"
          :rules="rules.pwd"
          label="密码"
          required
        ></v-text-field>

        <v-text-field
          v-if="!loginornot"
          variant="outlined"
          v-model="userPwdConfirm"
          :type="showPwd ? 'text' : 'password'"
          :rules="rules.pwdVerify"
          label="确认密码"
          required
        ></v-text-field>
      </v-form>
      <div class="d-flex justify-space-between">
        <v-btn
          v-if="loginornot"
          color="success"
          @click="login"
          :disabled="!valid"
          >确认</v-btn
        >
        <v-btn
          v-if="!loginornot"
          color="success"
          @click="regist"
          :disabled="!valid"
          >确认</v-btn
        >
        <v-checkbox
          class="pl-4"
          v-model="showPwd"
          hide-details
          density="compact"
          color="blue-grey-darken-2"
          label="显示密码"
        ></v-checkbox>
      </div>
    </v-card-text>
    <br />
  </v-card>
</template>