package Priv.wangjunqiang.config;

import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.mapper.MapperScannerConfigurer;
import org.springframework.context.annotation.Bean;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;

import javax.sql.DataSource;
import java.io.IOException;

public class MybatisConfig {

    @Bean
    public SqlSessionFactoryBean sqlSessionFactoryBean(DataSource dataSource)
        throws IOException {
        SqlSessionFactoryBean sqlSessionFactoryBean =
            new SqlSessionFactoryBean();

        sqlSessionFactoryBean.setDataSource(dataSource);

        sqlSessionFactoryBean.setTypeAliasesPackage("Priv.wangjunqiang.domain");

        // 设置mybatis Mapper映射文件路径
        PathMatchingResourcePatternResolver
            pathMatchingResourcePatternResolver =
            new PathMatchingResourcePatternResolver();

        Resource[] resources = pathMatchingResourcePatternResolver.getResources(
            "classpath:Priv/wangjunqiang/mapper/*.xml");

        sqlSessionFactoryBean.setMapperLocations(resources);

        return sqlSessionFactoryBean;
    }

    @Bean
    public MapperScannerConfigurer mapperScannerConfigurer() {
        MapperScannerConfigurer mapperScannerConfigurer =
            new MapperScannerConfigurer();
        mapperScannerConfigurer.setBasePackage("Priv.wangjunqiang.dao");
        return mapperScannerConfigurer;
    }
}
