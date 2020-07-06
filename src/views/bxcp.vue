<template>
  <div>
    <aside class="sidebar">
      <ul class="infinite-list" v-infinite-scroll='load' infinite-scroll-distance='3' style="overflow:auto">
        <li class="infinite-list-item" v-for='(i,index) in bxcpIndex' :key='index' @click='search(++index)'>
          {{i['No']}}:{{i['词牌名']}}
          <!-- <router-link :to="{name:'search',params:{cm:i}}" rel='i'>
            {{i}}
          </router-link> -->
        </li>
      <!--  <li>poem one</li>
       <li>poem one</li>
       <li>poem one</li>
       <li>poem one</li> -->
      </ul>
    </aside>
    
    <div class="page">
      <p v-if='cpBody'>{{cpBody['词牌名']}}•{{cpBody['词名']}}</p>
      <span>{{cpBody['作者']}}</span>
      
      <ul>
        <li v-for="(i,index) in cpBody['词体']" :key='index'>
          {{i}}
        </li>
      </ul>
    </div>
  
  </div>
</template>

<script type="text/javascript">
  export default {
    name:'bxcp',
    data() {
      return{
        bxcpIndex:[],
        cpBody:'',
      }
    },
    // created 
    created:function(){
      this.$axios({
        methods:'get',
        url:'http://127.0.0.1/bxcpIndex'
      }).then((res)=>{
        this.bxcpIndex = res.data  //待处理数据
      })
    },
    // 定义的方法
    methods:{
      // search function
      search:function(index){
        // alert(index)
        this.$axios({
          methods:'get',
          url:'http://127.0.0.1/search/'+index,    //注意拼写

        }).then((res)=>{
          let citi = res.data
          this.cpBody = citi;
        })
      },
    }
  }
</script>

<style type="text/css">
  .sidebar {
    float:left;     /* float浮动属性解决不并排显示*/
    width: 40%;
    margin:0;
    position: absolute;

    buttom:2px;
    background-color:$nav-color;
  }
  .infinite-list {
    margin: 0px;
    padding:0;
    width:190px;
    height:430px;
    border-radius:15px;
  }
  ul{
    border-buttom:3px solid;
  }
  li {
    width: 100%;
    display: inline-block;
    margin:0;
    list-style-type:none;
    border-radius: 3px;
  }
  li:hover{
    color: yellow;
  }
  .page{
    float: right;
    padding: 50px;
    position: absolute;
    width: 70%;
    height: 400px;
    font-size: 20px;
    left: 180px;
    overflow:auto;

  }
/*  .list-enter-active, .list-leave-active {
  transition: all 1s;
}
.list-enter, .list-leave-to
 .list-leave-active for below version 2.1.8  {
  opacity: 0;
  transform: translateY(30px);
}*/

</style>