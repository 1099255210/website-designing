<template>
  <form method="post" action="http://localhost:2145/login">
    <input type="text" name="userName">
    <input type="password" name="userPwd">
    <input type="submit" value="login">
  </form>
  <form method="post" action="http://localhost:2145/register">
    <input type="text" name="userName">
    <input type="password" name="userPwd">
    <input type="submit" value="register">
  </form>
</template>