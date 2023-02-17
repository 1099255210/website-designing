<script setup>
import axios from "axios";
import { userInfoStore } from '@/stores/stores.js'
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";
const userInfo = userInfoStore()
</script>

<script>
export default {
  data() {
    return {
      alertType: "",
      operated: false,
      msgTitle: "",
      msgText: "",
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
      axios.post("/api/login", data).then((res) => {
        console.log(res);
        this.msgTitle = res["data"]["type"];
        this.msgText = res["data"]["msg"];
        if (res["data"]["code"] == 0) {
          this.alertType = "success";
        } else {
          this.alertType = "error";
        }
        this.operated = true;
      });
    },
    regist() {
      const data = { userName: this.userName, userPwd: this.userPwd };
      axios.post("/api/regist", data).then((res) => {
        console.log(res);
        this.msgTitle = res["data"]["type"];
        this.msgText = res["data"]["msg"];
        if (res["data"]["code"] == 0) {
          this.alertType = "success";
          userInfo.setName(this.userName);
        } else {
          this.alertType = "error";
        }
        this.operated = true;
      });
    },
    getImageUrl(name) {
      return new URL(`../assets/${name}`, import.meta.url).href;
    },
    refreshMsg() {
      this.operated = false;
    }
  },
  mounted() {
    this.operated = false;
  }
};
</script>

<template>
  <v-fade-transition>
    <v-card>
      <v-img
        class="align-end text-white"
        height="190px"
        :src="getImageUrl('login-img.jpg')"
        cover
      >
        <v-card-text>
          <p class="text-h4">&nbsp;海报创作平台</p>
        </v-card-text>
      </v-img>
      <v-card-text>
        <v-btn-toggle v-model="loginornot" color="blue-grey-darken-2">
          <v-btn :value="true" @click="refreshMsg">登录</v-btn>
          <v-btn :value="false" @click="refreshMsg">注册</v-btn>
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
            >登录</v-btn
          >
          <v-btn
            v-if="!loginornot"
            color="success"
            @click="regist"
            :disabled="!valid"
            >注册</v-btn
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
  </v-fade-transition>
  <v-fade-transition>
    <v-alert
      v-model="operated"
      :type=alertType
      :title=msgTitle
      :text=msgText
    ></v-alert>
  </v-fade-transition>
  
</template>