<template>
	<p>词名：{{cm}}</p>
</template>
<script type="text/javascript">
	export default {
		name:'search',
		props:{
			cm:String,
		},
		data() {
			return{
				bxcp:{},

			}
		},
		// created 钩子一个实例被创建后执行代码
		// created:function(){
		// 	alert(this.cm)
		// }

	}
</script>