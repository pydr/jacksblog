
var vm = new Vue({
    el: "#breaking",
    delimiters: ['[[', ']]'],
    data: {
        recent_post: [],
    },

    mounted: function(){
	    this.get_recent_post();
    },

    methods: {

        get_recent_post: function(){
            // 获取最近更新文章列表
            axios.get('http://127.0.0.1:8000/recent_posts/', {
                responseType: 'json',
            }).then(response=>{
                this.recent_post = response.data;
            }).catch(error=>{
                console.log("最近更新加载失败！")
            })
        },

    }
});



var vm = new Vue({
    el: "#index_list",
    delimiters: ['[[', ']]'],
    data: {
        posts_list: [],
        recent_post: [],
    },

    mounted: function(){
	    this.get_index_list();
	    this.get_recent_post();
    },

    methods: {
        get_index_list: function(){
            // 获取首页文章列表
            axios.get('http://127.0.0.1:8000/posts/', {
                responseType: 'json',
            }).then(response=>{
                this.posts_list = response.data;
            }).catch(error=>{
                alert("网络连接超时，请稍后再试~")
            })
        },
        get_recent_post: function(){
            // 获取最近更新文章列表
            axios.get('http://127.0.0.1:8000/recent_posts/', {
                responseType: 'json',
            }).then(response=>{
                this.recent_post = response.data;
            }).catch(error=>{
                console.log("最近更新加载失败！")
            })
        },

    }
});

var vm = new Vue({
    el: "#index_list",
    delimiters: ['[[', ']]'],
    data: {
        writings: [],
        recent_post: [],
        categories: [],
    },

    mounted: function(){
	    this.get_content();
	    this.get_recent_post();
	    this.get_category();
    },

    methods: {
        get_content: function(){
            // 获取首页文章列表
            axios.get('http://127.0.0.1:8000/posts/', {
                responseType: 'json',
            }).then(response=>{
                this.writings = response.data;
            }).catch(error=>{
                alert("无法获取数据，请检查您的网络！")
            })
        },

        get_recent_post: function(){
            // 获取最近更新文章列表
            axios.get('http://127.0.0.1:8000/recent_posts/', {
                responseType: 'json',
            }).then(response=>{
                this.recent_post = response.data;
            }).catch(error=>{
                console.log("最近更新加载失败！")
            })
        },

        get_category: function(){
            // 获取最近更新文章列表
            axios.get('http://127.0.0.1:8000/categories/', {
                responseType: 'json',
            }).then(response=>{
                this.categories = response.data;
            }).catch(error=>{
                console.log("分类数据获取失败！")
            })
        },

        get_category: function(){
            // 获取最近更新文章列表
            axios.get('http://127.0.0.1:8000/categories/', {
                responseType: 'json',
            }).then(response=>{
                this.categories = response.data;
            }).catch(error=>{
                console.log("分类数据获取失败！")
            })
        },

    }
});