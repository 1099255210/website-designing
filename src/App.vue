<script setup>
import userInfo from './stores/stores'

const userStore = userInfo()

</script>

<template>
  <v-card>
    <v-app>
      <v-navigation-drawer
        expand-on-hover
        rail
      >
        <v-list>
          <!-- 
          <p class="body1" id="username">Hg</p>
          <p class="body2 text-medium-emphasis" id="email">1099255210@qq.com</p> -->
          <v-list-item
            title="Hg"
            subtitle="1099255210@qq.com"
          >
            <template #prepend>
              <v-avatar color="primary">Hg</v-avatar>
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
          <!-- <v-list-item title="Shared with me" value="shared"></v-list-item>
          <v-list-item prepend-icon="mdi-star" title="Starred" value="starred"></v-list-item> -->
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
  
</template>


<!-- <template>
  <v-app>

    <div class="nav_t" >
      <ul>
        <li class="nav_t_main">
          <RouterLink to="/">
            <img src="./assets/main-icon.png" alt="" srcset="" width="48">
          </RouterLink>
        </li>
        <input type="text" class="nav_t_search" >
        <li class="nav_t_doc">
          <RouterLink to="/doc">文档</RouterLink>
        </li>
      </ul>
    </div>

    <v-app-bar
      elevation="4"
    ></v-app-bar>

    <div class="nav_l" >
      <ul>
        <li>
          <div class="dividingline"></div>
        </li>
        <li>
          <RouterLink to="/community">设计社区</RouterLink>
        </li>
        <li>
          <RouterLink to="/postergen">商品海报生成</RouterLink>
        </li>
        <li>
          <RouterLink to="/gifgen">动态海报生成</RouterLink>
        </li>
        <li>
          <div class="dividingline"></div>
        </li>
        <li>
          <RouterLink to="/mydesign">我的设计</RouterLink>
        </li>
        <li>
          <RouterLink to="/myassets">我的素材</RouterLink>
        </li>
        <li>
          <RouterLink to="/myfavourite">我的收藏</RouterLink>
        </li>
        <li>
          <div class="dividingline"></div>
        </li>
        <li>
          <RouterLink to="/login">登录</RouterLink>
        </li>
        <li>
          <RouterLink to="/regist">注册</RouterLink>
        </li>
        <li>
          <RouterLink to="/test">测试</RouterLink>
        </li>
      </ul>
    </div>

    <div class="main_container">
      <RouterView />
    </div>

  </v-app>

</template>

<style scoped>

ul {
  list-style-type: none;
}

.nav_l a,
.nav_t a {
  display: block;
  color: black;
  text-decoration: none;
  line-height: 30px;
}

.nav_l a {
  padding-left: 20px;
  padding-right: 20px;
  padding-top: 10px;
  padding-bottom: 10px;
}

.nav_l a:hover {
  background-color: rgb(203, 203, 203);
  border-radius: 5px;
}

.nav_l {
  background-color: white;
  border-right-width: 1px;
  border-right-style: solid;
  border-color: rgb(130, 130, 130);
  height: 100%;
  width: 140px;
  position: fixed;
  left: 0;
  top: 100px;
  text-align: center;
  z-index: 1;
}

.nav_l ul {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.nav_l li {
  width: 100%;
}

.dividingline {
  margin-top: 20px;
  margin-bottom: 20px;
  width: 100%;
  
  border-style: solid;
  border-top: none;
  border-left: none;
  border-right: none;
  border-width: 1px;
  border-color: rgb(130, 130, 130);
}

.nav_t {
  /* background-color: rgb(12, 171, 168); */
  background-color: white;
  border-bottom-style: solid;
  border-bottom-width: 1px;
  border-color: rgb(130, 130, 130);
  margin: 0;
  height: 100px;
  width: 100%;
  position: fixed;
  left: 0;
  top: 0;
  display: flex;
  align-items: center;
  z-index: 2;
}

.nav_t ul {
  width: 100%;
  padding-left: 50px;
  padding-right: 50px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}


.main_container {
  position: absolute;
  top: 100px;
  left: 140px;
  width: 100% - 140px;
  height: 100% - 100px;
  margin: 50px;
}


</style> -->

<script>
export default {
  data() {
    return {
      items: [
        {icon: 'mdi-star', title:'设计社区', router:'/community'},
        {icon: 'mdi-star', title:'商品海报生成', router:'/postergen'},
        {icon: 'mdi-star', title:'动态海报生成', router:'/gifgen'},
        {icon: 'mdi-star', title:'我的设计', router:'/mydesign'},
        {icon: 'mdi-star', title:'我的素材', router:'/myassets'},
        {icon: 'mdi-star', title:'我的收藏', router:'/myfavourite'},
        {icon: 'mdi-star', title:'测试', router:'/test'},
      ]
    }
  }
}
</script>