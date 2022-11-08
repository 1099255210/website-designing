<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


<template>

  <!--顶部导航栏 -->
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
    </ul>
  </div>

  <!-- 页面中央渲染内容 -->
  <div class="main_container">
    <RouterView />
  </div>

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


</style>