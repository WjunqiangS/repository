package Priv.wangjunqiang.config;

import org.springframework.context.annotation.*;

@Configuration
@ComponentScan("Priv.wangjunqiang")
@PropertySource("classpath:jdbc.properties")
@Import({JdbcConfig.class, MybatisConfig.class})
@EnableAspectJAutoProxy
public class SpringConfig {
}
