package Priv.wangjunqiang.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurationSupport;

@Configuration
// 重点，要在SpringMvcConfig中把类扫描上
public class SpringMvcSupport extends WebMvcConfigurationSupport {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/pages/**").addResourceLocations(
            "classpath:/pages/");
        registry.addResourceHandler("/js/**").addResourceLocations("classpath:"
            + "/js/");
        registry.addResourceHandler("/css/**").addResourceLocations(
            "classpath:/css/");
    }
}
