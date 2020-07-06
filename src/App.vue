<template>
  <div class="container">
    <header class='navbar'>
      <span class="site-name">mmpoem.cn</span>
      <router-link to="/">主页</router-link> |
      <router-link to="/bxcp">白香词谱</router-link> |
      <router-link to="/other">待完善</router-link> |
    </header>
    <router-view class='content'/>
  </div>
</template>

<script type="text/javascript">
  export default {
  data() {
    return {

    }
  },
  methods: {

  }
  }
</script>

<style >
  .container {
    width: 100%;
    height: 100%;

  }
  header {
    z-index:20;
    margin:0;
    padding: 0;
    position:fixed;
    width: 100%;
    height: 45px;
    border-bottom: 1px solid ;
    font-size:200%;
  }
  .content {
    position: relative;
    left: 0;
    top:45px;
  }
    a {
    text-decoration: none;
    color:inherit;
  }
  a:hover{
    text-decoration: underline;
    line-height:5.4px;

  }

</style>
