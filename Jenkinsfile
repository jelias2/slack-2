@Library('utils@master') _
import com.lmig.intl.cloud.jenkins.util.EnvConfigUtil
//('linux') Tell jenkins to run on worker nodes and not master
node('linux') {



  stage('Checkout'){
    //Gather code from BB
    checkout scm
  }


  stage('Docker Build'){
      //Make sure the docker image builds
       sh 'docker build -t flask-api .'
    }

    stage('Push image to ECR'){

       withAWS(credentials:'aws-cred'){
          //Get the login credentials, this is essental
          sh("eval \$(aws ecr get-login --no-include-email | sed 's|https://||')")
          //Tag and push the lastest image to the ECR
          sh 'docker tag flask-api:latest 467193240914.dkr.ecr.eu-west-1.amazonaws.com/flask_api:latest'
          sh 'docker push 467193240914.dkr.ecr.eu-west-1.amazonaws.com/flask-api:latest'
      }
    }
//  }

//    stage('Deploy image to ECS'){

//      withAWS(credentials: 'aws-cred'){

        //Create a new cluster, In future get input for region and name
        // sh 'aws ecs create-cluster --region eu-west-1 --cluster-name cluster-2'
        //
        //
        // //Creates a service with in the cluster and deploys intern
        // sh '''aws ecs create-service \
        //     --region eu-west-1 \
        //     --cluster cluster-2 \
        //     --service-name cmd-service \
        //     --task-definition intern-task:1 \
        //     --desired-count 1 \
        //     --launch-type "FARGATE" \
        //     --network-configuration "awsvpcConfiguration={ \
        //       subnets=[subnet-9f10b7d6], \
        //       securityGroups=[sg-7a834406] \
        //       }"'''

        // FORMAT: aws ecs run-task --task-definition task-def-name --cluster cluster-name
        //sh 'aws ecs run-task --task-definition intern-task --cluster intl-intern-cluster --network-mode awsvpc'
  //    }
  //  }



  //  }
       //configure registry
       // docker.withRegistry('https://467193240914.ecr.eu-west-1.amazonaws.com/jacob-api', 'ecr:eu-west-1:86c8f5ec-1ce1-4e94-80c2-18e23bbd724a') {
       //
       //     //build image
       //     def customImage = docker.build("my-image:${env.BUILD_ID}")
       //
       //     //push image
       //     customImage.push()

}
