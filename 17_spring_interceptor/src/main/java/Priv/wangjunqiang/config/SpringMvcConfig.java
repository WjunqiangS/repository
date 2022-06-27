package Priv.wangjunqiang.config;

import Priv.wangjunqiang.controller.interceptor.ProjectInterceptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
@ComponentScan("Priv.wangjunqiang.controller")
@EnableWebMvc
public class SpringMvcConfig implements WebMvcConfigurer{

    @Autowired
    private ProjectInterceptor projectInterceptor;

    // 添加拦截器
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(projectInterceptor).addPathPatterns("/users",
            "/users/*");
    }

    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
    }
}
