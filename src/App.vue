<script setup>
import { userInfoStore } from '@/stores/stores'
import Logintest from './components/Logintest.vue'
import { storeToRefs } from 'pinia'

const store = userInfoStore()
const { userName, userEmail, subtitle, loginStatus, short } = storeToRefs(store)

</script>

<template>
  <v-card>
    <v-app>
      <v-navigation-drawer
        expand-on-hover
        rail
      >
        <v-list>
          <v-list-item
            :title="userName"
            :subtitle="subtitle"
          >
            <template #prepend>
              <v-avatar color="#7a7a7a" style="cursor:pointer" v-if="loginStatus" title="切换账号" @click="cancelLogin">
                <p style="color: aliceblue" class="text-caption" v-if="loginStatus">{{ short }}</p>
              </v-avatar>
              <v-avatar color="#7a7a7a" v-if="!loginStatus" @click="loginDialog=true" title="登录" style="cursor:pointer">
                <p class="text-caption" v-if="loginStatus">{{ short }}</p>
              </v-avatar>
            </template>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list density="compact" nav>
          <v-list-item 
            v-for="item in items"
            :prepend-icon="item.icon"
            :key="item.title"
            :title="item.title"
            :value="item.title"
            :to="item.router">
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-app-bar color="grey-lighten-4"></v-app-bar>
      <v-main class="bg-grey-lighten-5">
        <v-container class="py-10 px-10" fluid>
          <RouterView/>
        </v-container>
      </v-main>
    </v-app>
  </v-card>
  
  <v-dialog
    width="500px"
    v-model="loginDialog"
  >
    <Logintest @closeLogin="loginDialog=false" />
  </v-dialog>

</template>

<script>
export default {
  data() {
    return {
      items: [
        { icon: 'mdi-account-group', title:'设计社区', router:'/community' },
        { icon: 'mdi-format-paint', title:'商品海报生成', router:'/postergen' },
        { icon: 'mdi-movie', title:'动态海报生成', router:'/gifgen' },
        { icon: 'mdi-lead-pencil', title:'我的设计', router:'/mydesign' },
        { icon: 'mdi-folder-image', title:'我的素材', router:'/myassets' },
        { icon: 'mdi-star', title:'我的收藏', router:'/myfavourite' },
        { icon: 'mdi-ab-testing', title:'测试', router:'/test' },
        { icon: 'mdi-ab-testing', title:'测试2', router:'/test2'},
      ],
      loginDialog: false,
    }
  },
  methods: {
    cancelLogin() {
      const userInfo = userInfoStore()
      userInfo.setStatus("登录", "点击左侧圆点登录", "点击左侧圆点登录", 0, "");
      this.loginDialog = true;
    },
  },
  components: {
    Logintest,
  }
}
</script>