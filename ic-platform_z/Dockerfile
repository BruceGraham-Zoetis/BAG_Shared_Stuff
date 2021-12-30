# syntax=docker/dockerfile:experimental

#
# Build Stage
#

FROM ghcr.io/zoetisdenmark/build-java-11-mvn-3:latest AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN --mount=type=cache,target=/root/.m2 --mount=type=secret,id=github-token \
    /mvn.sh package -Dmaven.test.skip

#
# Run stage
#

FROM ghcr.io/zoetisdenmark/runtime-java-11 AS runtime
WORKDIR /app
COPY --from=build /app/target/*.jar /app/ic-platform.jar
ENTRYPOINT ["java", "-jar", "/app/ic-platform.jar"]
