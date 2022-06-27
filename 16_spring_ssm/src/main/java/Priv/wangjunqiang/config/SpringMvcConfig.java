package Priv.wangjunqiang.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;

@Configuration
@ComponentScan({"Priv.wangjunqiang.controller", "Priv.wangjunqiang.config"})
@EnableWebMvc
public class SpringMvcConfig {
}